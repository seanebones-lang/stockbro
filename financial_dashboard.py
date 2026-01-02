"""
Real-time Financial Dashboard - Web Interface
Supports stocks and crypto via Polygon.io API (rebranded to Massive) and Alpha Vantage
Enhanced with xAI Grok 4.1 Fast reasoning for advanced analysis
Built with Dash (Plotly) for interactive web interface
Optimized for reliability and performance as of December 2025
"""

import os
import time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import requests  # For Alpha Vantage API calls
from polygon import RESTClient
from polygon.websocket import WebSocketClient, Market
import threading
import queue

# Optional xAI Grok SDK import
try:
    from xai_sdk import Client as XAIClient
    XAI_AVAILABLE = True
except ImportError:
    XAI_AVAILABLE = False
    XAIClient = None

# Dash and Plotly imports
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

# Positive and negative keywords for simple sentiment analysis (fallback)
POSITIVE_WORDS = [
    'gain', 'rise', 'up', 'positive', 'growth', 'success',
    'beat', 'surge', 'boost', 'strong', 'rally', 'profit',
    'increase', 'bullish', 'optimistic', 'expansion'
]
NEGATIVE_WORDS = [
    'loss', 'fall', 'down', 'negative', 'decline', 'miss',
    'drop', 'weak', 'slump', 'crash', 'plunge', 'deficit',
    'decrease', 'bearish', 'pessimistic', 'recession'
]

# Shared variables (thread-safe)
latest_price = None
price_lock = threading.Lock()
news_data = []
sentiment_score = 0
sentiment_class = 'Neutral'
ws_clients = {}  # Store WebSocket clients by ticker


def get_historical_data(source, client, av_key, rest_ticker, is_crypto, base, quote='USD', days=30):
    """
    Fetch historical daily data. Switches between Polygon and Alpha Vantage (2025 compliant endpoints).
    Explanation: This function retrieves open, high, low, close, and volume (OHLCV) data for the past N days.
    It uses daily aggregates to show price trends, which helps in understanding market volatility and patterns.
    For stocks, it fetches adjusted closes; for crypto, market-specific daily series.
    """
    end = datetime.today().strftime('%Y-%m-%d')
    start = (datetime.today() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    if source == 'polygon':
        try:
            aggs = client.get_aggs(rest_ticker, multiplier=1, timespan='day', from_=start, to=end)
            df = pd.DataFrame(aggs)
            if df.empty:
                return df
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            return df
        except Exception as e:
            print(f"Polygon error fetching historical data: {e}")
            return pd.DataFrame()
    
    elif source == 'alphavantage':
        try:
            # Alpha Vantage rate limiting
            time.sleep(0.2)

            if is_crypto:
                url = (
                    f"https://www.alphavantage.co/query?"
                    f"function=DIGITAL_CURRENCY_DAILY&"
                    f"symbol={base}&"
                    f"market={quote}&"
                    f"apikey={av_key}"
                )
            else:
                url = (
                    f"https://www.alphavantage.co/query?"
                    f"function=TIME_SERIES_DAILY&"
                    f"symbol={base}&"
                    f"apikey={av_key}"
                )

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check for API errors
            if 'Error Message' in data:
                print(f"Alpha Vantage API error: {data['Error Message']}")
                return pd.DataFrame()
            if 'Note' in data:
                print(f"Alpha Vantage rate limit: {data['Note']}")
                return pd.DataFrame()

            # Extract time series data
            if is_crypto:
                time_series_key = 'Time Series (Digital Currency Daily)'
            else:
                time_series_key = 'Time Series (Daily)'

            if time_series_key not in data:
                print(f"Alpha Vantage: No time series data found for {base}")
                return pd.DataFrame()

            # Convert to DataFrame
            df = pd.DataFrame.from_dict(data[time_series_key], orient='index')
            df.index = pd.to_datetime(df.index)
            df = df.sort_index()

            # Normalize column names
            if is_crypto:
                df.columns = [col.split('(')[0].strip().split('.')[1].strip().lower() for col in df.columns]
            else:
                df.columns = [col.split('.')[1].strip().lower() for col in df.columns]

            # Convert to float
            df = df.astype(float)

            # Limit to requested days
            if len(df) > days:
                df = df.tail(days)

            # Ensure we have required columns
            required_cols = ['open', 'high', 'low', 'close', 'volume']
            if not all(col in df.columns for col in required_cols):
                print(f"Alpha Vantage: Missing required columns. Got: {df.columns.tolist()}")
                return pd.DataFrame()

            return df

        except requests.exceptions.RequestException as e:
            print(f"Alpha Vantage network error: {e}")
            return pd.DataFrame()
        except Exception as e:
            print(f"Alpha Vantage error fetching historical data: {e}")
            return pd.DataFrame()

    else:
        return pd.DataFrame()


def get_news(source, client, av_key, rest_ticker, base, limit=5):
    """
    Fetch recent news. Uses Polygon or Alpha Vantage NEWS_SENTIMENT.
    Explanation: News items include titles, summaries, URLs, and publish dates, providing context on market events.
    This helps explain price movements, e.g., a surge due to positive earnings reports.
    Limit is set to 5 for recency and relevance.
    """
    if source == 'polygon':
        try:
            news = list(client.list_ticker_news(rest_ticker, limit=limit))
            # Normalize to dict format for consistency
            normalized = []
            for article in news:
                normalized.append({
                    'title': getattr(article, 'title', ''),
                    'description': getattr(article, 'description', ''),
                    'article_url': getattr(article, 'article_url', ''),
                    'published_utc': getattr(article, 'published_utc', '')
                })
            return normalized
        except Exception as e:
            print(f"Polygon error fetching news: {e}")
            return []
    
    elif source == 'alphavantage':
        try:
            # Alpha Vantage rate limiting
            time.sleep(0.2)

            url = (
                f"https://www.alphavantage.co/query?"
                f"function=NEWS_SENTIMENT&"
                f"tickers={base}&"
                f"limit={limit}&"
                f"apikey={av_key}"
            )

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check for API errors
            if 'Error Message' in data:
                print(f"Alpha Vantage API error: {data['Error Message']}")
                return []
            if 'Note' in data:
                print(f"Alpha Vantage rate limit: {data['Note']}")
                return []

            # Extract news feed
            items = data.get('feed', [])
            normalized = []
            for item in items:
                normalized.append({
                    'title': item.get('title', ''),
                    'description': item.get('summary', ''),
                    'article_url': item.get('url', ''),
                    'published_utc': item.get('time_published', ''),
                    'sentiment_score': item.get('overall_sentiment_score', None),
                    'sentiment_label': item.get('overall_sentiment_label', None)
                })
            return normalized

        except requests.exceptions.RequestException as e:
            print(f"Alpha Vantage network error: {e}")
            return []
        except Exception as e:
            print(f"Alpha Vantage error fetching news: {e}")
            return []

    else:
        return []


def get_sentiment(source, news, av_key, base, xai_key=None):
    """
    Get sentiment: Custom for Polygon, built-in AV, or Grok 4.1 Fast if enabled.
    Explanation: Sentiment score ranges from -1 (negative) to 1 (positive), classifying market mood.
    For Grok, it uses high-effort reasoning for nuanced insights, e.g., weighing regulatory news impacts.
    Fallback uses keyword counts for quick approximation.
    """
    if xai_key and XAI_AVAILABLE and news:
        try:
            xai_client = XAIClient(api_key=xai_key)
            
            # Prepare news text for analysis
            news_text = ""
            for i, article in enumerate(news[:5], 1):
                title = article.get('title', '') if isinstance(article, dict) else getattr(article, 'title', '')
                desc = article.get('description', '') if isinstance(article, dict) else getattr(article, 'description', '')
                news_text += f"Article {i}: {title}\n{desc}\n\n"

            chat = xai_client.chat.create(
                model="grok-4.1-fast-reasoning",
                reasoning_effort="high",
                messages=[
                    {"role": "system", "content": "You are a financial analyst. Provide sentiment score (-1 to 1) and reasoned insights."},
                    {"role": "user", "content": f"Analyze sentiment and insights for this news: {news_text}"}
                ]
            )
            response = chat.sample()
            content = response.content
            
            # Parse response
            score = 0.0
            if "Score:" in content:
                try:
                    score_str = content.split("Score:")[1].split("\n")[0].strip()
                    score = float(score_str)
                except (ValueError, IndexError):
                    pass

            classification = 'Neutral'
            if "Sentiment:" in content:
                try:
                    classification = content.split("Sentiment:")[1].split("\n")[0].strip()
                    if classification not in ['Positive', 'Negative', 'Neutral']:
                        classification = 'Positive' if score > 0.1 else 'Negative' if score < -0.1 else 'Neutral'
                except IndexError:
                    classification = 'Positive' if score > 0.1 else 'Negative' if score < -0.1 else 'Neutral'
            else:
                classification = 'Positive' if score > 0.1 else 'Negative' if score < -0.1 else 'Neutral'

            reasoning_trace = getattr(response, 'reasoning_content', None)
            if reasoning_trace:
                print(f"\n🤖 Grok 4.1 Fast Reasoning Trace:\n{reasoning_trace}")

            return score, classification
        except Exception as e:
            print(f"xAI Grok error: {e}. Falling back to basic sentiment.")

    if source == 'polygon':
        if not news:
            return 0, 'No News'
        scores = []
        for article in news:
            if isinstance(article, dict):
                text = (article.get('title', '') or '') + ' ' + (article.get('description', '') or '')
            else:
                text = (getattr(article, 'title', '') or '') + ' ' + (getattr(article, 'description', '') or '')
            text_lower = text.lower()
            pos_count = sum(text_lower.count(word) for word in POSITIVE_WORDS)
            neg_count = sum(text_lower.count(word) for word in NEGATIVE_WORDS)
            score = pos_count - neg_count
            scores.append(score)
        avg_score = np.mean(scores) if scores else 0
        classification = 'Positive' if avg_score > 0 else 'Negative' if avg_score < 0 else 'Neutral'
        return avg_score, classification
    
    elif source == 'alphavantage':
        if not news:
            return 0, 'No News'

        # Alpha Vantage provides sentiment scores in news items
        sentiment_scores = []
        for article in news:
            score = article.get('sentiment_score') if isinstance(article, dict) else None
            if score is not None:
                sentiment_scores.append(float(score))

        if sentiment_scores:
            avg_score = np.mean(sentiment_scores)
            if avg_score > 0.1:
                classification = 'Positive'
            elif avg_score < -0.1:
                classification = 'Negative'
            else:
                classification = 'Neutral'
            return avg_score, classification
        else:
            # Fallback to keyword analysis
            return get_sentiment('polygon', news, None, base, None)

    else:
        return 0, 'Neutral'


def get_latest_trade(source, client, av_key, is_crypto, base, quote='USD'):
    """
    Fetch latest trade: Polygon for WS-capable, AV for REAL_TIME_PRICE.
    Explanation: Provides the most recent trade price, reflecting current market value.
    For real-time, Polygon uses WebSockets; AV polls every minute.
    This data is crucial for intraday decisions.
    """
    if source == 'polygon':
        try:
            if is_crypto:
                trade = client.get_last_crypto_trade(from_=base, to=quote)
                return trade.last.price if trade and trade.last else None
            else:
                quote_obj = client.get_last_trade(base)
                return quote_obj.price if quote_obj else None
        except Exception as e:
            print(f"Polygon error fetching latest trade: {e}")
            return None
    
    elif source == 'alphavantage':
        try:
            # Alpha Vantage rate limiting
            time.sleep(0.2)

            if is_crypto:
                url = (
                    f"https://www.alphavantage.co/query?"
                    f"function=CRYPTO_INTRADAY&"
                    f"symbol={base}&"
                    f"market={quote}&"
                    f"interval=1min&"
                    f"apikey={av_key}"
                )
            else:
                url = (
                    f"https://www.alphavantage.co/query?"
                    f"function=GLOBAL_QUOTE&"
                    f"symbol={base}&"
                    f"apikey={av_key}"
                )

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check for API errors
            if 'Error Message' in data:
                print(f"Alpha Vantage API error: {data['Error Message']}")
                return None
            if 'Note' in data:
                print(f"Alpha Vantage rate limit: {data['Note']}")
                return None

            if is_crypto:
                time_series = data.get('Time Series Crypto (1min)', {})
                if not time_series:
                    return None
                latest_key = sorted(time_series.keys())[-1]
                latest_data = time_series[latest_key]
                return float(latest_data.get('4. close', 0))
            else:
                global_quote = data.get('Global Quote', {})
                if not global_quote:
                    return None
                price_str = global_quote.get('05. price', '0')
                return float(price_str) if price_str else None

        except requests.exceptions.RequestException as e:
            print(f"Alpha Vantage network error: {e}")
            return None
        except Exception as e:
            print(f"Alpha Vantage error fetching latest trade: {e}")
            return None

    else:
        return None


def websocket_handler(ws_client, ticker, msg_queue):
    """
    Callback for WebSocket messages (Polygon only).
    """
    def handle_msg(messages):
        global latest_price
        for msg in messages:
            if hasattr(msg, 'event'):
                event_type = msg.event
                if (event_type == 'T' or event_type.startswith('X')) and hasattr(msg, 'price'):
                    with price_lock:
                        latest_price = msg.price
                    size = getattr(msg, 'size', 'N/A')
                    print(f"Real-time update: {ticker} trade at ${msg.price:.2f} (Size: {size})")

    try:
        ws_client.run(handle_msg=handle_msg)
    except Exception as e:
        print(f"WebSocket error: {e}")


def start_websocket(is_crypto, ticker_ws, api_key):
    """
    Start WebSocket (Polygon only).
    """
    market = Market.Crypto if is_crypto else Market.Stocks
    prefix = 'XT.' if is_crypto else 'T.'
    subscriptions = [f"{prefix}{ticker_ws}"]
    ws_client = WebSocketClient(api_key=api_key, market=market, subscriptions=subscriptions)
    msg_queue = queue.Queue()
    thread = threading.Thread(target=websocket_handler, args=(ws_client, ticker_ws, msg_queue))
    thread.daemon = True
    thread.start()
    return ws_client


def calculate_rsi(df, period=14):
    """Calculate Relative Strength Index (RSI)."""
    if df.empty or 'close' not in df.columns:
        return pd.Series(dtype=float)
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_macd(df, fast=12, slow=26, signal=9):
    """Calculate MACD (Moving Average Convergence Divergence)."""
    if df.empty or 'close' not in df.columns:
        return pd.Series(dtype=float), pd.Series(dtype=float), pd.Series(dtype=float)
    ema_fast = df['close'].ewm(span=fast, adjust=False).mean()
    ema_slow = df['close'].ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram


def calculate_bollinger_bands(df, period=20, std_dev=2):
    """Calculate Bollinger Bands."""
    if df.empty or 'close' not in df.columns:
        return pd.Series(dtype=float), pd.Series(dtype=float), pd.Series(dtype=float)
    sma = df['close'].rolling(window=period).mean()
    std = df['close'].rolling(window=period).std()
    upper_band = sma + (std * std_dev)
    lower_band = sma - (std * std_dev)
    return upper_band, sma, lower_band


def calculate_statistics(df, current_price=None):
    """Calculate key financial statistics."""
    if df.empty or 'close' not in df.columns:
        return {}
    
    stats = {}
    stats['current_price'] = current_price if current_price else df['close'].iloc[-1]
    stats['high_52w'] = df['high'].max() if 'high' in df.columns else None
    stats['low_52w'] = df['low'].min() if 'low' in df.columns else None
    stats['avg_volume'] = df['volume'].mean() if 'volume' in df.columns else None
    stats['price_change'] = ((df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0] * 100) if len(df) > 1 else 0
    stats['volatility'] = (df['close'].pct_change().std() * np.sqrt(252) * 100) if len(df) > 1 else 0
    stats['52w_range'] = ((stats['current_price'] - stats['low_52w']) / (stats['high_52w'] - stats['low_52w']) * 100) if stats['high_52w'] and stats['low_52w'] and stats['high_52w'] != stats['low_52w'] else None
    
    # Moving averages
    stats['ma_7'] = df['close'].rolling(7).mean().iloc[-1] if len(df) >= 7 else None
    stats['ma_30'] = df['close'].rolling(30).mean().iloc[-1] if len(df) >= 30 else None
    
    return stats


# Dash App Setup
app = dash.Dash(__name__)

# Dark mode styles
dark_mode_styles = {
    'backgroundColor': '#1a1a1a',
    'color': '#e0e0e0',
    'minHeight': '100vh',
    'padding': '20px'
}

light_mode_styles = {
    'backgroundColor': '#ffffff',
    'color': '#2c3e50',
    'minHeight': '100vh',
    'padding': '20px'
}

app.layout = html.Div(id='main-container', children=[
    html.Div([
        html.Div([
            html.H1("📊 Financial Dashboard", id='title', style={'textAlign': 'center', 'marginBottom': '10px'}),
            html.Div([
                html.Label("🌙 Dark Mode:", style={'marginRight': '10px', 'fontWeight': 'bold'}),
                dcc.RadioItems(
                    id='dark-mode-toggle',
                    options=[
                        {'label': 'On', 'value': 'on'},
                        {'label': 'Off', 'value': 'off'}
                    ],
                    value='off',
                    inline=True,
                    style={'display': 'inline-block'}
                ),
            ], style={'textAlign': 'center', 'marginBottom': '15px'}),
            html.P(
                "Powered by Dash (Plotly) - The leading framework for building analytical web apps in Python as of December 2025. "
                "This interactive dashboard provides real-time financial data visualization with explanations for each component.",
                id='subtitle',
                style={'textAlign': 'center', 'marginBottom': '30px'}
            ),
        ]),
    ], id='header', style={'padding': '20px', 'marginBottom': '20px', 'borderRadius': '10px'}),

    html.Div([
        html.Div([
            html.Label("Asset Type:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Dropdown(
                id='asset-type',
                options=[
                    {'label': 'Stock', 'value': 'stock'},
                    {'label': 'Crypto', 'value': 'crypto'}
                ],
                value='stock',
                style={'marginBottom': '15px'}
            ),
        ], style={'width': '32%', 'display': 'inline-block', 'marginRight': '2%'}),

        html.Div([
            html.Label("Ticker/Pair (e.g., AAPL or BTC-USD):", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Input(
                id='ticker',
                type='text',
                value='AAPL',
                style={'width': '100%', 'padding': '8px', 'marginBottom': '15px'}
            ),
        ], style={'width': '32%', 'display': 'inline-block', 'marginRight': '2%'}),

        html.Div([
            html.Label("Data Source:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Dropdown(
                id='source',
                options=[
                    {'label': 'Polygon.io', 'value': 'polygon'},
                    {'label': 'Alpha Vantage', 'value': 'alphavantage'}
                ],
                value='polygon',
                style={'marginBottom': '15px'}
            ),
        ], style={'width': '32%', 'display': 'inline-block'}),
    ]),

    html.Div([
        html.Div([
            html.Label("Polygon API Key:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Input(
                id='polygon-api-key',
                type='password',
                placeholder='Enter Polygon API key (or leave empty to use env var)',
                style={'width': '100%', 'padding': '8px', 'marginBottom': '15px'}
            ),
        ], style={'width': '32%', 'display': 'inline-block', 'marginRight': '2%'}),

        html.Div([
            html.Label("Alpha Vantage API Key:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.Input(
                id='av-api-key',
                type='password',
                placeholder='Enter Alpha Vantage API key (or leave empty to use env var)',
                style={'width': '100%', 'padding': '8px', 'marginBottom': '15px'}
            ),
        ], style={'width': '32%', 'display': 'inline-block', 'marginRight': '2%'}),

        html.Div([
            html.Label("Use xAI Grok 4.1 Fast?", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            dcc.RadioItems(
                id='use-grok',
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'}
                ],
                value='no',
                style={'marginBottom': '10px'}
            ),
            html.Div(id='xai-key-container', children=[
                html.Label("xAI API Key:", style={'fontWeight': 'bold', 'marginBottom': '5px', 'marginTop': '10px'}),
                dcc.Input(
                    id='xai-api-key',
                    type='password',
                    placeholder='Enter your xAI API key here',
                    style={'width': '100%', 'padding': '8px', 'marginBottom': '15px'}
                ),
            ], style={'display': 'none'}),
        ], style={'width': '32%', 'display': 'inline-block'}),
    ]),

    html.Div([
        html.Label("Enable Real-Time Updates (Polygon only):", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
        dcc.RadioItems(
            id='real-time',
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            value='no',
            style={'marginBottom': '20px'}
        ),
    ]),

    html.Button(
        '🔄 Refresh Dashboard',
        id='refresh-button',
        n_clicks=0,
        style={
            'backgroundColor': '#3498db',
            'color': 'white',
            'padding': '10px 20px',
            'border': 'none',
            'borderRadius': '5px',
            'cursor': 'pointer',
            'fontSize': '16px',
            'marginBottom': '20px'
        }
    ),

    html.Hr(),

    # Statistics Summary Row
    html.Div([
        html.Div(id='stats-summary', children=[]),
    ], id='stats-section', style={'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px'}),

    # Charts Row - Two columns
    html.Div([
        html.Div([
            html.H3("📊 Price Chart", id='chart-title', style={'marginBottom': '10px'}),
            html.P(
                "Interactive line chart with closing prices and moving averages.",
                id='chart-desc',
                style={'fontStyle': 'italic', 'marginBottom': '10px', 'fontSize': '12px'}
            ),
            dcc.Graph(id='price-chart'),
        ], style={'width': '48%', 'display': 'inline-block', 'marginRight': '2%', 'verticalAlign': 'top'}),

        html.Div([
            html.H3("📈 Volume Chart", id='volume-title', style={'marginBottom': '10px'}),
            html.P(
                "Trading volume over time. High volume often indicates significant price movements.",
                id='volume-desc',
                style={'fontStyle': 'italic', 'marginBottom': '10px', 'fontSize': '12px'}
            ),
            dcc.Graph(id='volume-chart'),
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    ], id='charts-row', style={'marginBottom': '30px'}),

    # Candlestick Chart
    html.Div([
        html.H3("🕯️ Candlestick Chart", id='candle-title', style={'marginBottom': '10px'}),
        html.P(
            "OHLC candlestick chart showing open, high, low, and close prices. Green = price up, Red = price down.",
            id='candle-desc',
            style={'fontStyle': 'italic', 'marginBottom': '10px', 'fontSize': '12px'}
        ),
        dcc.Graph(id='candlestick-chart'),
    ], id='candle-section', style={'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px'}),

    # Technical Indicators Row
    html.Div([
        html.Div([
            html.H3("📊 RSI (Relative Strength Index)", id='rsi-title', style={'marginBottom': '10px'}),
            html.P("RSI above 70 = overbought, below 30 = oversold", style={'fontSize': '12px', 'color': '#7f8c8d', 'marginBottom': '10px'}),
            dcc.Graph(id='rsi-chart', style={'height': '300px'}),
        ], style={'width': '32%', 'display': 'inline-block', 'padding': '15px', 'borderRadius': '10px', 'marginRight': '1%', 'verticalAlign': 'top'}, id='rsi-section'),
        
        html.Div([
            html.H3("📊 MACD", id='macd-title', style={'marginBottom': '10px'}),
            html.P("Moving Average Convergence Divergence indicator", style={'fontSize': '12px', 'color': '#7f8c8d', 'marginBottom': '10px'}),
            dcc.Graph(id='macd-chart', style={'height': '300px'}),
        ], style={'width': '32%', 'display': 'inline-block', 'padding': '15px', 'borderRadius': '10px', 'marginRight': '1%', 'verticalAlign': 'top'}, id='macd-section'),
        
        html.Div([
            html.H3("📊 Bollinger Bands", id='bb-title', style={'marginBottom': '10px'}),
            html.P("Price volatility bands around moving average", style={'fontSize': '12px', 'color': '#7f8c8d', 'marginBottom': '10px'}),
            dcc.Graph(id='bollinger-chart', style={'height': '300px'}),
        ], style={'width': '32%', 'display': 'inline-block', 'padding': '15px', 'borderRadius': '10px', 'verticalAlign': 'top'}, id='bb-section'),
    ], style={'marginBottom': '30px'}),

    # Historical Data Table
    html.Div([
        html.H3("📋 Historical Data Table", id='hist-title', style={'marginBottom': '10px'}),
        html.P(
            "Detailed OHLCV data for the last 30 days. Sort by clicking column headers.",
            id='hist-desc',
            style={'fontStyle': 'italic', 'marginBottom': '10px', 'fontSize': '12px'}
        ),
        html.Div(id='historical-table', children=[]),
    ], id='hist-section', style={'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px'}),

    html.Div([
        html.H3("📰 Recent News", id='news-title', style={'marginBottom': '10px'}),
        html.P(
            "Latest articles with links. Explains potential price drivers, e.g., earnings beats, regulatory changes, or market events.",
            id='news-desc',
            style={'fontStyle': 'italic', 'marginBottom': '10px'}
        ),
        html.Div(id='news-section', children=[]),
    ], id='news-section-container', style={'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px'}),

    html.Div([
        html.H3("💭 Sentiment Analysis", id='sentiment-title', style={'marginBottom': '10px'}),
        html.P(
            "Sentiment score and classification from news analysis. Positive (>0) suggests bullish outlook; "
            "Negative (<0) suggests bearish. With Grok enabled, includes AI reasoning traces.",
            id='sentiment-desc',
            style={'fontStyle': 'italic', 'marginBottom': '10px'}
        ),
        html.Div(id='sentiment', children=[]),
    ], id='sentiment-section', style={'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px'}),

    html.Div([
        html.H3("💰 Latest Price", id='price-title', style={'marginBottom': '10px'}),
        html.P(
            "Real-time trade value. For investment decisions, compare to historical highs/lows and moving averages.",
            id='price-desc',
            style={'fontStyle': 'italic', 'marginBottom': '10px'}
        ),
        html.Div(id='latest-price', children=[]),
    ], id='price-section', style={'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px'}),

    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # 60 seconds
        n_intervals=0,
        disabled=True
    )
])


# Callback to show/hide xAI key input
@app.callback(
    Output('xai-key-container', 'style'),
    Input('use-grok', 'value')
)
def toggle_xai_key(use_grok):
    if use_grok == 'yes':
        return {'display': 'block', 'marginTop': '10px'}
    return {'display': 'none'}

# Callback for dark mode
@app.callback(
    [Output('main-container', 'style'),
     Output('header', 'style'),
     Output('title', 'style'),
     Output('subtitle', 'style'),
     Output('hist-section', 'style'),
     Output('candle-section', 'style'),
     Output('news-section-container', 'style'),
     Output('sentiment-section', 'style'),
     Output('price-section', 'style'),
     Output('hist-title', 'style'),
     Output('chart-title', 'style'),
     Output('news-title', 'style'),
     Output('sentiment-title', 'style'),
     Output('price-title', 'style'),
     Output('hist-desc', 'style'),
     Output('chart-desc', 'style'),
     Output('news-desc', 'style'),
     Output('sentiment-desc', 'style'),
     Output('price-desc', 'style')],
    Input('dark-mode-toggle', 'value')
)
def update_dark_mode(dark_mode):
    is_dark = dark_mode == 'on'
    
    if is_dark:
        return (
            dark_mode_styles,
            {'padding': '20px', 'marginBottom': '20px', 'borderRadius': '10px', 'backgroundColor': '#2d2d2d'},
            {'textAlign': 'center', 'marginBottom': '10px', 'color': '#e0e0e0'},
            {'textAlign': 'center', 'marginBottom': '30px', 'color': '#b0b0b0'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#2d2d2d'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#2d2d2d'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#2d2d2d'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#2d2d2d'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#2d2d2d'},
            {'marginBottom': '10px', 'color': '#e0e0e0'},
            {'marginBottom': '10px', 'color': '#e0e0e0'},
            {'marginBottom': '10px', 'color': '#e0e0e0'},
            {'marginBottom': '10px', 'color': '#e0e0e0'},
            {'marginBottom': '10px', 'color': '#e0e0e0'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#b0b0b0'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#b0b0b0'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#b0b0b0'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#b0b0b0'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#b0b0b0'}
        )
    else:
        return (
            light_mode_styles,
            {'padding': '20px', 'marginBottom': '20px', 'borderRadius': '10px', 'backgroundColor': '#ecf0f1'},
            {'textAlign': 'center', 'marginBottom': '10px', 'color': '#2c3e50'},
            {'textAlign': 'center', 'marginBottom': '30px', 'color': '#7f8c8d'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#f8f9fa'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#f8f9fa'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#f8f9fa'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#f8f9fa'},
            {'marginBottom': '30px', 'padding': '15px', 'borderRadius': '10px', 'backgroundColor': '#f8f9fa'},
            {'marginBottom': '10px', 'color': '#2c3e50'},
            {'marginBottom': '10px', 'color': '#2c3e50'},
            {'marginBottom': '10px', 'color': '#2c3e50'},
            {'marginBottom': '10px', 'color': '#2c3e50'},
            {'marginBottom': '10px', 'color': '#2c3e50'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#7f8c8d'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#7f8c8d'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#7f8c8d'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#7f8c8d'},
            {'fontStyle': 'italic', 'marginBottom': '10px', 'color': '#7f8c8d'}
        )

@app.callback(
    [Output('stats-summary', 'children'),
     Output('historical-table', 'children'),
     Output('candlestick-chart', 'figure'),
     Output('volume-chart', 'figure'),
     Output('price-chart', 'figure'),
     Output('rsi-chart', 'figure'),
     Output('macd-chart', 'figure'),
     Output('bollinger-chart', 'figure'),
     Output('news-section', 'children'),
     Output('sentiment', 'children'),
     Output('latest-price', 'children'),
     Output('interval-component', 'disabled')],
    [Input('refresh-button', 'n_clicks'),
     Input('interval-component', 'n_intervals')],
    [State('asset-type', 'value'),
     State('ticker', 'value'),
     State('source', 'value'),
     State('use-grok', 'value'),
     State('real-time', 'value'),
     State('xai-api-key', 'value'),
     State('polygon-api-key', 'value'),
     State('av-api-key', 'value'),
     State('dark-mode-toggle', 'value')]
)
def update_dashboard(n_clicks, n_intervals, asset_type, ticker, source, use_grok, real_time, xai_key_input, polygon_key_input, av_key_input, dark_mode):
    """Update dashboard with latest data."""
    if not ticker:
        empty_fig = go.Figure()
        empty_fig.add_annotation(text="Please enter a ticker symbol", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        return (
            html.Div("Please enter a ticker symbol.", style={'color': 'red'}),  # stats-summary
            html.P("No data available."),  # historical-table
            empty_fig,  # candlestick-chart
            empty_fig,  # volume-chart
            empty_fig,  # price-chart
            empty_fig,  # rsi-chart
            empty_fig,  # macd-chart
            empty_fig,  # bollinger-chart
            html.P("No data available."),  # news-section
            html.P("No data available."),  # sentiment
            html.P("No data available."),  # latest-price
            True  # interval-component disabled
        )

    is_crypto = asset_type == 'crypto'
    use_grok_bool = use_grok == 'yes'
    real_time_bool = real_time == 'yes'
    is_dark = dark_mode == 'on'

    # Format ticker
    if is_crypto:
        if '-' in ticker:
            base, quote = ticker.split('-')
        else:
            base = ticker[:-3] if len(ticker) > 3 else ticker
            quote = ticker[-3:] if len(ticker) > 3 else 'USD'
    else:
        base = ticker.upper()
        quote = 'USD'

    rest_ticker = f"X:{base.upper()}{quote.upper()}" if is_crypto else base.upper()
    ticker_ws = f"{base.upper()}-{quote.upper()}" if is_crypto else base.upper()

    # Get API keys - prioritize input over environment variable
    api_key = polygon_key_input if polygon_key_input else (os.getenv('POLYGON_API_KEY') if source == 'polygon' else None)
    av_key = av_key_input if av_key_input else (os.getenv('ALPHAVANTAGE_API_KEY') if source == 'alphavantage' else None)
    xai_key = xai_key_input if xai_key_input else (os.getenv('XAI_API_KEY') if use_grok_bool else None)

    if not api_key and source == 'polygon':
        empty_fig = go.Figure()
        empty_fig.add_annotation(text="Please enter Polygon API key", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        return (
            html.P("Error: Please enter Polygon API key above or set POLYGON_API_KEY environment variable.", style={'color': 'red'}),  # stats-summary
            html.P("No data available."),  # historical-table
            empty_fig,  # candlestick-chart
            empty_fig,  # volume-chart
            empty_fig,  # price-chart
            empty_fig,  # rsi-chart
            empty_fig,  # macd-chart
            empty_fig,  # bollinger-chart
            html.P("No data available."),  # news-section
            html.P("No data available."),  # sentiment
            html.P("No data available."),  # latest-price
            True  # interval-component disabled
        )

    if not av_key and source == 'alphavantage':
        empty_fig = go.Figure()
        empty_fig.add_annotation(text="Please enter Alpha Vantage API key", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
        return (
            html.Div("Error: Please enter Alpha Vantage API key above or set ALPHAVANTAGE_API_KEY environment variable.", style={'color': 'red'}),  # stats-summary
            html.P("No data available."),  # historical-table
            empty_fig,  # candlestick-chart
            empty_fig,  # volume-chart
            empty_fig,  # price-chart
            empty_fig,  # rsi-chart
            empty_fig,  # macd-chart
            empty_fig,  # bollinger-chart
            html.P("No data available."),  # news-section
            html.P("No data available."),  # sentiment
            html.P("No data available."),  # latest-price
            True  # interval-component disabled
        )

    client = RESTClient(api_key) if source == 'polygon' and api_key else None

    # Start WebSocket if needed
    ws_key = f"{ticker_ws}_{source}"
    if real_time_bool and source == 'polygon' and api_key:
        if ws_key not in ws_clients:
            try:
                ws_clients[ws_key] = start_websocket(is_crypto, ticker_ws, api_key)
            except Exception as e:
                print(f"WebSocket error: {e}")

    # Fetch data
    df = get_historical_data(source, client, av_key, rest_ticker, is_crypto, base, quote)

    # Historical table
    if not df.empty:
        header_style = {'backgroundColor': '#3498db', 'color': 'white', 'fontWeight': 'bold'} if not is_dark else {'backgroundColor': '#2d2d2d', 'color': '#e0e0e0', 'fontWeight': 'bold'}
        cell_style = {'textAlign': 'left', 'padding': '10px', 'backgroundColor': '#ffffff', 'color': '#2c3e50'} if not is_dark else {'textAlign': 'left', 'padding': '10px', 'backgroundColor': '#1a1a1a', 'color': '#e0e0e0'}
        table = dash_table.DataTable(
            data=df.reset_index().to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.reset_index().columns],
            style_table={'overflowX': 'auto'},
            style_cell=cell_style,
            style_header=header_style
        )
    else:
        error_color = '#e74c3c' if not is_dark else '#ff6b6b'
        table = html.P("No historical data available.", style={'color': error_color})

    # Calculate statistics
    stats_html = []
    if not df.empty and 'close' in df.columns:
        current_price_val = df['close'].iloc[-1]
        prev_price = df['close'].iloc[-2] if len(df) > 1 else current_price_val
        price_change = current_price_val - prev_price
        price_change_pct = ((current_price_val - prev_price) / prev_price * 100) if prev_price > 0 else 0
        
        high_30d = df['high'].max() if 'high' in df.columns else None
        low_30d = df['low'].min() if 'low' in df.columns else None
        avg_price = df['close'].mean()
        avg_volume = df['volume'].mean() if 'volume' in df.columns else None
        
        change_color = '#27ae60' if price_change >= 0 else '#e74c3c'
        text_color = '#2c3e50' if not is_dark else '#e0e0e0'
        bg_color = '#f8f9fa' if not is_dark else '#2d2d2d'
        
        stats_html = html.Div([
            html.Div([
                html.H4("Current Price", style={'margin': '0', 'fontSize': '14px', 'color': text_color}),
                html.P(f"${current_price_val:.2f}", style={'margin': '5px 0', 'fontSize': '24px', 'fontWeight': 'bold', 'color': text_color}),
                html.P(f"{price_change:+.2f} ({price_change_pct:+.2f}%)", style={'margin': '0', 'color': change_color, 'fontWeight': 'bold'})
            ], style={'textAlign': 'center', 'padding': '15px', 'backgroundColor': bg_color, 'borderRadius': '8px', 'margin': '5px'}),
            html.Div([
                html.H4("30-Day High", style={'margin': '0', 'fontSize': '14px', 'color': text_color}),
                html.P(f"${high_30d:.2f}" if high_30d else "N/A", style={'margin': '5px 0', 'fontSize': '20px', 'fontWeight': 'bold', 'color': text_color})
            ], style={'textAlign': 'center', 'padding': '15px', 'backgroundColor': bg_color, 'borderRadius': '8px', 'margin': '5px'}),
            html.Div([
                html.H4("30-Day Low", style={'margin': '0', 'fontSize': '14px', 'color': text_color}),
                html.P(f"${low_30d:.2f}" if low_30d else "N/A", style={'margin': '5px 0', 'fontSize': '20px', 'fontWeight': 'bold', 'color': text_color})
            ], style={'textAlign': 'center', 'padding': '15px', 'backgroundColor': bg_color, 'borderRadius': '8px', 'margin': '5px'}),
            html.Div([
                html.H4("Average Price", style={'margin': '0', 'fontSize': '14px', 'color': text_color}),
                html.P(f"${avg_price:.2f}", style={'margin': '5px 0', 'fontSize': '20px', 'fontWeight': 'bold', 'color': text_color})
            ], style={'textAlign': 'center', 'padding': '15px', 'backgroundColor': bg_color, 'borderRadius': '8px', 'margin': '5px'}),
            html.Div([
                html.H4("Avg Volume", style={'margin': '0', 'fontSize': '14px', 'color': text_color}),
                html.P(f"{avg_volume:,.0f}" if avg_volume else "N/A", style={'margin': '5px 0', 'fontSize': '20px', 'fontWeight': 'bold', 'color': text_color})
            ], style={'textAlign': 'center', 'padding': '15px', 'backgroundColor': bg_color, 'borderRadius': '8px', 'margin': '5px'}),
        ], style={'display': 'flex', 'justifyContent': 'space-around', 'flexWrap': 'wrap'})
    else:
        stats_html = html.P("No statistics available.", style={'color': '#e74c3c' if not is_dark else '#ff6b6b'})

    # Price chart
    if not df.empty and 'close' in df.columns:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['close'],
            mode='lines',
            name='Close Price',
            line=dict(color='#3498db', width=2)
        ))
        df['MA7'] = df['close'].rolling(window=7).mean()
        df['MA30'] = df['close'].rolling(window=min(30, len(df))).mean()
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['MA7'],
            mode='lines',
            name='7-Day MA',
            line=dict(color='#e67e22', width=2, dash='dash')
        ))
        if len(df) >= 30:
            fig.add_trace(go.Scatter(
                x=df.index,
                y=df['MA30'],
                mode='lines',
                name='30-Day MA',
                line=dict(color='#9b59b6', width=2, dash='dot')
            ))
        chart_template = 'plotly_dark' if is_dark else 'plotly_white'
        fig.update_layout(
            title=f'{ticker_ws} Price Chart',
            xaxis_title='Date',
            yaxis_title='Price (USD)',
            hovermode='x unified',
            template=chart_template,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400
        )
    else:
        fig = go.Figure()
        fig.add_annotation(
            text="No data available for chart",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )

    # Volume chart
    if not df.empty and 'volume' in df.columns:
        volume_fig = go.Figure()
        volume_fig.add_trace(go.Bar(
            x=df.index,
            y=df['volume'],
            name='Volume',
            marker_color='#3498db'
        ))
        chart_template = 'plotly_dark' if is_dark else 'plotly_white'
        volume_fig.update_layout(
            title=f'{ticker_ws} Trading Volume',
            xaxis_title='Date',
            yaxis_title='Volume',
            template=chart_template,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400
        )
    else:
        volume_fig = go.Figure()
        volume_fig.add_annotation(
            text="No volume data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )

    # Candlestick chart
    if not df.empty and all(col in df.columns for col in ['open', 'high', 'low', 'close']):
        candle_fig = go.Figure(data=go.Candlestick(
            x=df.index,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name='OHLC'
        ))
        chart_template = 'plotly_dark' if is_dark else 'plotly_white'
        candle_fig.update_layout(
            title=f'{ticker_ws} Candlestick Chart',
            xaxis_title='Date',
            yaxis_title='Price (USD)',
            template=chart_template,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500,
            xaxis_rangeslider_visible=False
        )
    else:
        candle_fig = go.Figure()
        candle_fig.add_annotation(
            text="No OHLC data available for candlestick chart",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )

    # News
    global news_data
    news_data = get_news(source, client, av_key, rest_ticker, base)
    if news_data:
        news_list = []
        for article in news_data:
            title = article.get('title', 'N/A') if isinstance(article, dict) else getattr(article, 'title', 'N/A')
            desc = article.get('description', '') if isinstance(article, dict) else getattr(article, 'description', '')
            url = article.get('article_url', '') if isinstance(article, dict) else getattr(article, 'article_url', '')
            pub_date = article.get('published_utc', '') if isinstance(article, dict) else getattr(article, 'published_utc', '')
            
            desc_short = desc[:200] + '...' if len(desc) > 200 else desc
            
            title_color = '#2c3e50' if not is_dark else '#e0e0e0'
            desc_color = '#7f8c8d' if not is_dark else '#b0b0b0'
            date_color = '#95a5a6' if not is_dark else '#808080'
            bg_color = '#f8f9fa' if not is_dark else '#2d2d2d'
            hr_color = '#e0e0e0' if not is_dark else '#404040'
            
            news_list.append(html.Div([
                html.H4(title, style={'color': title_color, 'marginBottom': '5px'}),
                html.P(desc_short, style={'color': desc_color, 'marginBottom': '5px'}),
                html.A("Read More", href=url, target='_blank', style={'color': '#3498db', 'marginRight': '10px'}) if url else None,
                html.Span(f"Published: {pub_date}", style={'color': date_color, 'fontSize': '12px'}),
                html.Hr(style={'margin': '15px 0', 'borderColor': hr_color})
            ], style={'marginBottom': '15px', 'padding': '10px', 'backgroundColor': bg_color, 'borderRadius': '5px'}))
        news_display = html.Div(news_list)
    else:
        error_color = '#e74c3c' if not is_dark else '#ff6b6b'
        news_display = html.P("No recent news available.", style={'color': error_color})

    # Sentiment
    global sentiment_score, sentiment_class
    sentiment_score, sentiment_class = get_sentiment(source, news_data, av_key, base, xai_key)
    
    sentiment_color = '#27ae60' if sentiment_class == 'Positive' else '#e74c3c' if sentiment_class == 'Negative' else '#95a5a6'
    score_color = '#7f8c8d' if not is_dark else '#b0b0b0'
    sentiment_display = html.Div([
        html.P(
            f"Sentiment: {sentiment_class}",
            style={'fontSize': '20px', 'fontWeight': 'bold', 'color': sentiment_color, 'marginBottom': '5px'}
        ),
        html.P(f"Score: {sentiment_score:.2f}", style={'color': score_color})
    ])

    # Latest price
    with price_lock:
        current_price = latest_price

    if not current_price:
        current_price = get_latest_trade(source, client, av_key, is_crypto, base, quote)

    if current_price:
        price_color = '#2c3e50' if not is_dark else '#e0e0e0'
        price_display = html.P(
            f"${current_price:.2f}",
            style={'fontSize': '32px', 'fontWeight': 'bold', 'color': price_color}
        )
    else:
        error_color = '#e74c3c' if not is_dark else '#ff6b6b'
        price_display = html.P("No price data available.", style={'color': error_color})

    # RSI Chart
    if not df.empty and 'close' in df.columns:
        rsi = calculate_rsi(df)
        rsi_fig = go.Figure()
        rsi_fig.add_trace(go.Scatter(
            x=df.index,
            y=rsi,
            mode='lines',
            name='RSI',
            line=dict(color='#3498db', width=2)
        ))
        rsi_fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought (70)")
        rsi_fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold (30)")
        chart_template = 'plotly_dark' if is_dark else 'plotly_white'
        rsi_fig.update_layout(
            title='RSI (14-period)',
            xaxis_title='Date',
            yaxis_title='RSI',
            yaxis_range=[0, 100],
            template=chart_template,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300
        )
    else:
        rsi_fig = go.Figure()
        rsi_fig.add_annotation(text="No data available", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)

    # MACD Chart
    if not df.empty and 'close' in df.columns:
        macd, signal, histogram = calculate_macd(df)
        macd_fig = go.Figure()
        macd_fig.add_trace(go.Scatter(x=df.index, y=macd, mode='lines', name='MACD', line=dict(color='#3498db')))
        macd_fig.add_trace(go.Scatter(x=df.index, y=signal, mode='lines', name='Signal', line=dict(color='#e67e22')))
        macd_fig.add_trace(go.Bar(x=df.index, y=histogram, name='Histogram', marker_color='#95a5a6'))
        chart_template = 'plotly_dark' if is_dark else 'plotly_white'
        macd_fig.update_layout(
            title='MACD',
            xaxis_title='Date',
            yaxis_title='Value',
            template=chart_template,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300
        )
    else:
        macd_fig = go.Figure()
        macd_fig.add_annotation(text="No data available", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)

    # Bollinger Bands Chart
    if not df.empty and 'close' in df.columns:
        upper, middle, lower = calculate_bollinger_bands(df)
        bb_fig = go.Figure()
        bb_fig.add_trace(go.Scatter(x=df.index, y=upper, mode='lines', name='Upper Band', line=dict(color='#e74c3c', dash='dash')))
        bb_fig.add_trace(go.Scatter(x=df.index, y=middle, mode='lines', name='SMA (20)', line=dict(color='#3498db')))
        bb_fig.add_trace(go.Scatter(x=df.index, y=lower, mode='lines', name='Lower Band', line=dict(color='#e74c3c', dash='dash')))
        bb_fig.add_trace(go.Scatter(x=df.index, y=df['close'], mode='lines', name='Close Price', line=dict(color='#2c3e50' if not is_dark else '#e0e0e0')))
        chart_template = 'plotly_dark' if is_dark else 'plotly_white'
        bb_fig.update_layout(
            title='Bollinger Bands',
            xaxis_title='Date',
            yaxis_title='Price (USD)',
            template=chart_template,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300
        )
    else:
        bb_fig = go.Figure()
        bb_fig.add_annotation(text="No data available", xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)

    # Enable/disable interval based on real-time setting
    interval_disabled = not real_time_bool

    return stats_html, table, candle_fig, volume_fig, fig, rsi_fig, macd_fig, bb_fig, news_display, sentiment_display, price_display, interval_disabled


if __name__ == "__main__":
    print("=" * 60)
    print("Financial Dashboard - Web Interface")
    print("Powered by Dash (Plotly)")
    print("=" * 60)
    print("\nStarting web server...")
    print("Open your browser and navigate to: http://127.0.0.1:8050")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(debug=True, host='127.0.0.1', port=8050)
