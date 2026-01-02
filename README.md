# StockBro - Real-time Financial Dashboard

A powerful **web-based** financial dashboard for real-time stock and cryptocurrency monitoring, powered by **Polygon.io API** (rebranded to Massive), **Alpha Vantage API**, and **xAI Grok 4.1 Fast** reasoning. Built with **Dash (Plotly)** for interactive web visualization. Optimized for reliability and performance as of December 2025.

---

## What is StockBro?

**StockBro** is a comprehensive, real-time financial data visualization platform that combines traditional market data with cutting-edge AI-powered sentiment analysis. It's a fully-featured web application that transforms raw financial data into actionable insights through interactive charts, technical indicators, news analysis, and AI-driven market sentiment evaluation.

Unlike command-line tools or static reports, StockBro provides an intuitive, browser-based interface that makes financial analysis accessible to both technical and non-technical users. Whether you're monitoring a single stock, tracking cryptocurrency movements, or analyzing market sentiment, StockBro delivers professional-grade financial analysis tools in an easy-to-use package.

---

## What Does It Do?

StockBro aggregates and visualizes financial data from multiple sources, providing:

### Core Functionality

- **📊 Real-Time Market Monitoring**: Track live prices for stocks and cryptocurrencies with WebSocket streaming (Polygon) or polling (Alpha Vantage)
- **📈 Historical Data Analysis**: Visualize 30 days of OHLCV (Open, High, Low, Close, Volume) data with interactive charts
- **🕯️ Advanced Charting**: Multiple chart types including line charts, candlestick charts, and volume analysis
- **📰 News Integration**: Fetch and display recent news articles related to your selected asset with clickable links
- **💭 Sentiment Analysis**: Three-tier sentiment analysis system:
  - **xAI Grok 4.1 Fast**: AI-powered reasoning with step-by-step analysis traces
  - **Alpha Vantage**: Built-in AI sentiment scores
  - **Keyword-Based**: Fast sentiment analysis using positive/negative word detection
- **📉 Technical Indicators**: Professional technical analysis tools:
  - RSI (Relative Strength Index) with overbought/oversold markers
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands for volatility analysis
  - Moving averages (7-day and 30-day)
- **📋 Interactive Data Tables**: Sortable, scrollable tables with complete historical data
- **🌙 Dark Mode**: Comfortable viewing in any lighting condition
- **🔄 Auto-Refresh**: Optional automatic updates every 60 seconds for real-time monitoring

### Key Features

- **Dual Data Source Support**: Choose between Polygon.io (premium features, WebSocket streaming) or Alpha Vantage (free tier, built-in sentiment)
- **Multi-Asset Support**: Monitor both traditional stocks (NYSE, NASDAQ) and cryptocurrencies (Bitcoin, Ethereum, etc.)
- **Thread-Safe Architecture**: Secure concurrent updates for real-time data streaming
- **Robust Error Handling**: Graceful degradation and clear error messages
- **Rate Limit Management**: Automatic rate limiting to respect API constraints
- **Zero Configuration Required**: Works out of the box with API keys

---

## Who Is This For?

StockBro is designed for a diverse range of users:

### 🎯 Primary Users

1. **Individual Investors & Traders**
   - Day traders monitoring real-time price movements
   - Swing traders analyzing technical indicators and sentiment
   - Long-term investors tracking portfolio positions
   - Crypto enthusiasts following digital asset markets

2. **Financial Analysts & Researchers**
   - Market researchers needing quick data visualization
   - Analysts comparing sentiment across different sources
   - Students learning financial analysis techniques
   - Journalists writing market analysis pieces

3. **Developers & Data Scientists**
   - Developers building financial applications
   - Data scientists prototyping trading strategies
   - FinTech startups needing a dashboard solution
   - Hobbyists exploring financial APIs

4. **Educators & Students**
   - Finance professors teaching market analysis
   - Students learning about technical analysis
   - Coding bootcamp participants building portfolio projects
   - Self-learners exploring financial technology

### 👥 User Profiles

- **The Casual Investor**: Wants to quickly check stock prices and recent news without complexity
- **The Active Trader**: Needs real-time data, technical indicators, and sentiment analysis for trading decisions
- **The Researcher**: Requires comprehensive data visualization and analysis tools
- **The Developer**: Wants a clean, well-documented codebase to build upon or integrate
- **The Learner**: Seeking to understand financial markets through hands-on visualization

---

## Why Use StockBro?

### 🎯 Problem It Solves

The financial data landscape is fragmented and complex. Getting comprehensive market information typically requires:
- Multiple subscriptions to expensive services
- Complex API integrations
- Technical expertise to build custom tools
- Time-consuming data aggregation from various sources

**StockBro solves this by providing a single, unified platform that combines:**
- Real-time price data
- Historical analysis
- News aggregation
- AI-powered sentiment analysis
- Technical indicators
- Professional visualizations

### ✨ Key Benefits

1. **🚀 Quick Setup, Zero Complexity**
   - Install dependencies, add API keys, and you're running in minutes
   - No complex configuration or infrastructure required
   - Web-based interface means no app installations needed

2. **💰 Cost-Effective**
   - Works with free-tier API keys (Alpha Vantage offers free access)
   - No subscription fees or hidden costs
   - Self-hosted means you control your data and costs

3. **🔒 Privacy & Security**
   - Runs locally on your machine
   - API keys stored securely (environment variables)
   - No data sent to third-party servers (except API providers)
   - Open-source code you can audit

4. **🎨 Professional Visualizations**
   - Interactive Plotly charts with zoom, pan, and hover details
   - Publication-ready visualizations
   - Export capabilities for reports and presentations

5. **🤖 AI-Powered Insights**
   - Optional xAI Grok integration for advanced sentiment analysis
   - Step-by-step reasoning traces for transparency
   - Multiple sentiment analysis methods for comparison

6. **🔄 Flexible & Extensible**
   - Support for multiple data sources (switch between Polygon and Alpha Vantage)
   - Modular architecture makes customization easy
   - Well-documented codebase for developers

7. **📱 Accessible Anywhere**
   - Web-based interface works on any device with a browser
   - Run locally or deploy to a server for remote access
   - Responsive design adapts to different screen sizes

### 🎓 Use Cases

- **Portfolio Monitoring**: Track your holdings in real-time with automatic refresh
- **Market Research**: Analyze historical trends and sentiment for investment decisions
- **Trading Strategy Development**: Test technical indicators and sentiment analysis
- **News-Driven Trading**: Monitor news and sentiment before making trades
- **Educational Projects**: Learn about financial markets through interactive visualization
- **Due Diligence**: Quick analysis of assets before investment
- **Market Timing**: Identify entry and exit points using technical indicators
- **Crypto Trading**: Monitor cryptocurrency markets with the same tools as stocks

---

## Features

- **🌐 Web-Based Interface**: Interactive Dash (Plotly) web dashboard - no command line needed!
- **Dual Data Source Support**: Choose between Polygon.io or Alpha Vantage APIs
- **Real-time Price Updates**: WebSocket streaming for live price updates (Polygon only; Alpha Vantage uses polling)
- **Historical Data Analysis**: Fetch and visualize OHLCV data with interactive tables
- **Interactive Charts**: Plotly-powered charts with zoom, pan, and hover details
- **News Integration**: Fetch recent news articles with clickable links
- **Advanced Sentiment Analysis**: 
  - **xAI Grok 4.1 Fast reasoning** for AI-powered sentiment with step-by-step traces
  - Built-in AI sentiment scores with Alpha Vantage NEWS_SENTIMENT
  - Keyword-based sentiment analysis for Polygon
- **AI-Powered Market Analysis**: Grok 4.1 Fast provides reasoned insights, trends, and forecasts
- **Multi-Asset Support**: Works with both stocks (e.g., AAPL) and cryptocurrencies (e.g., BTC-USD)
- **Technical Indicators**: RSI, MACD, Bollinger Bands, and moving averages
- **Thread-Safe**: Secure concurrent updates for real-time data
- **Error Handling**: Robust error handling and reconnection logic
- **Rate Limit Management**: Automatic rate limiting for Alpha Vantage (5 calls/minute free tier)
- **Auto-Refresh**: Optional automatic updates every 60 seconds
- **Dark Mode**: Comfortable viewing in any lighting condition

---

## Requirements

- Python 3.8 or higher
- **Polygon.io API key** (get one at [massive.com](https://massive.com) - formerly polygon.io) **OR**
- **Alpha Vantage API key** (get one at [alphavantage.co](https://www.alphavantage.co/support/#api-key) - free tier: 25 calls/day, 5 calls/minute)
- **xAI API key** (optional, get one at [x.ai/api](https://x.ai/api) - for Grok 4.1 Fast reasoning)

---

## Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/seanebones-lang/stockbro.git
   cd stockbro
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - `polygon-api-client` (v1.14+) - For Polygon REST API and WebSocket connections
   - `pandas` (v2.0+) - For data processing
   - `matplotlib` (v3.7+) - For charting (optional, for exports)
   - `numpy` (v1.24+) - For numerical operations
   - `requests` (v2.31+) - For Alpha Vantage API calls
   - `xai-sdk` (v1.0+) - For xAI Grok 4.1 Fast reasoning (optional)
   - `dash` (v2.14+) - For web interface (Plotly Dash)
   - `plotly` (v5.17+) - For interactive charts

4. **Set up your API key(s)**:
   
   **For Polygon.io:**
   - Option 1: Set as environment variable (recommended)
     ```bash
     export POLYGON_API_KEY=your_api_key_here
     ```
   - Option 2: Enter in the web interface when prompted
   
   **For Alpha Vantage:**
   - Option 1: Set as environment variable (recommended)
     ```bash
     export ALPHAVANTAGE_API_KEY=your_api_key_here
     ```
   - Option 2: Enter in the web interface when prompted
   
   **For xAI Grok (Optional):**
   - Option 1: Set as environment variable (recommended)
     ```bash
     export XAI_API_KEY=your_api_key_here
     ```
   - Option 2: Enter in the web interface when Grok is enabled
   
   **Note**: You only need one data source API key (Polygon or Alpha Vantage). xAI Grok is optional and enhances analysis.

---

## Usage

### Starting the Web Dashboard

Run the dashboard:
```bash
python financial_dashboard.py
```

Or use the convenience script:
```bash
./run_dashboard.sh
```

The dashboard will start a web server at `http://127.0.0.1:8050`. Open this URL in your web browser to access the interactive dashboard.

### Web Interface Features

The dashboard provides a user-friendly web interface with:

1. **Configuration Panel**:
   - **Asset Type**: Dropdown to select `stock` or `crypto`
   - **Ticker/Pair**: Text input for ticker symbol (e.g., `AAPL` for stocks, `BTC-USD` for crypto)
   - **Data Source**: Choose between `Polygon.io` or `Alpha Vantage`
   - **xAI Grok**: Toggle to enable Grok 4.1 Fast reasoning (requires XAI_API_KEY)
   - **Real-Time Updates**: Toggle for automatic refresh (Polygon only)
   - **Dark Mode**: Toggle between light and dark themes

2. **Data Visualization**:
   - **Statistics Summary**: Key metrics including current price, 30-day high/low, average price, and volume
   - **Historical Data Table**: Interactive table showing OHLCV data
   - **Price Chart**: Interactive Plotly chart with 7-day and 30-day moving averages
     - Hover for detailed values
     - Zoom and pan to explore specific periods
     - Download chart as PNG
   - **Candlestick Chart**: OHLC visualization with green/red candles
   - **Volume Chart**: Trading volume over time
   - **Technical Indicators**: RSI, MACD, and Bollinger Bands charts
   - **Recent News**: Latest articles with clickable links
   - **Sentiment Analysis**: Score and classification with color coding
   - **Latest Price**: Real-time or latest available price

3. **Auto-Refresh**: 
   - When "Real-Time Updates" is enabled, the dashboard automatically refreshes every 60 seconds
   - Manual refresh available via the "Refresh Dashboard" button

### Example Usage

1. **Start the server**:
   ```bash
   python financial_dashboard.py
   ```

2. **Open your browser** to `http://127.0.0.1:8050`

3. **Configure the dashboard**:
   - Select "Stock" or "Crypto" from Asset Type dropdown
   - Enter ticker symbol (e.g., `AAPL` for Apple stock, `BTC-USD` for Bitcoin)
   - Choose data source (Polygon or Alpha Vantage)
   - Enter your API key(s) or ensure they're set as environment variables
   - Optionally enable xAI Grok for advanced analysis
   - Enable real-time updates if using Polygon
   - Toggle dark mode for comfortable viewing

4. **Click "Refresh Dashboard"** to load data

5. **Interact with the charts**:
   - Hover over data points for detailed values
   - Use toolbar to zoom, pan, or download charts
   - Click and drag to zoom into specific time periods
   - Switch between light and dark modes

### Dashboard Components

The web dashboard displays:

- **📊 Statistics Summary**: Key metrics in an easy-to-read card layout
- **📈 Historical Data Table**: Interactive table with last 30 days of OHLCV data
  - Sortable columns
  - Scrollable for large datasets
- **📊 Price Chart**: Interactive Plotly line chart
  - Close price line (blue)
  - 7-day moving average (orange, dashed)
  - 30-day moving average (purple, dotted)
  - Hover tooltips with exact values
  - Zoom and pan controls
- **🕯️ Candlestick Chart**: OHLC visualization
  - Green candles for price increases
  - Red candles for price decreases
  - Full OHLC data visualization
- **📊 Volume Chart**: Trading volume bars
  - Visual representation of trading activity
  - Correlation with price movements
- **📊 Technical Indicators**:
  - **RSI**: Relative Strength Index with 70 (overbought) and 30 (oversold) markers
  - **MACD**: Moving Average Convergence Divergence with signal line and histogram
  - **Bollinger Bands**: Upper band, middle (SMA), and lower band with price overlay
- **📰 Recent News**: Latest articles
  - Titles and descriptions
  - Clickable "Read More" links
  - Publication dates
- **💭 Sentiment Analysis**: 
  - Color-coded sentiment (Green=Positive, Red=Negative, Gray=Neutral)
  - Score from -1 to 1
  - With Grok: Includes AI reasoning traces in console
- **💰 Latest Price**: Large, prominent display of current price

---

## API Key Setup

### Polygon.io (Massive)

1. Sign up at [massive.com](https://massive.com) (formerly polygon.io)
2. Get your API key from the dashboard
3. Free tier includes:
   - Limited REST API calls
   - Basic WebSocket streaming (rate-limited)
   - Historical data access
   - News feeds

For production use, consider upgrading to a paid plan for higher rate limits.

### Alpha Vantage

1. Sign up at [alphavantage.co](https://www.alphavantage.co/support/#api-key)
2. Get your free API key (instant access)
3. Free tier includes (as of 2025):
   - **25 API calls per day**
   - **5 API calls per minute** (rate limit)
   - Historical data (stocks and crypto)
   - News with built-in AI sentiment analysis
   - Real-time quotes (via polling)

**Important**: Alpha Vantage free tier has strict rate limits. The script automatically enforces a minimum 12-second interval between calls to respect the 5 calls/minute limit.

**Comparison**:
- **Polygon**: Better for real-time streaming, higher rate limits (paid tiers)
- **Alpha Vantage**: Free tier with built-in sentiment analysis, good for basic use cases

### xAI Grok 4.1 Fast (Optional)

1. Sign up at [x.ai/api](https://x.ai/api)
2. Get your API key from the dashboard
3. Free tier includes (as of December 2025):
   - Access to Grok 4.1 Fast reasoning model
   - Rate limits based on tier
   - 2M context window for deep analysis
   - Reasoning traces for transparency

**Features**:
- **Advanced Sentiment Analysis**: AI-powered sentiment with step-by-step reasoning
- **Market Insights**: Comprehensive analysis of trends and forecasts
- **Reasoning Effort Levels**: Choose between low, medium, or high for complexity
- **Reasoning Traces**: See how Grok arrives at conclusions

**Note**: Grok adds latency (TTFT ~1-2s in fast mode) and costs per token. Check [x.ai/pricing](https://x.ai/pricing) for details.

---

## Features in Detail

### Real-time Streaming
- Uses WebSocket connections for low-latency price updates (Polygon only)
- Automatically handles reconnections
- Thread-safe price updates using locks
- Separate subscriptions for stocks (`T.AAPL`) and crypto (`XT.BTC-USD`)

### Sentiment Analysis
- **xAI Grok 4.1 Fast** (if enabled): Advanced AI reasoning with step-by-step traces
  - Analyzes news context and provides reasoned sentiment scores
  - Returns classification with detailed reasoning
  - Configurable reasoning effort (low/medium/high)
  - Shows reasoning traces for transparency
- **Alpha Vantage**: Built-in AI sentiment scores from NEWS_SENTIMENT endpoint
  - Provides sentiment scores and labels per article
  - Overall sentiment aggregation
- **Polygon**: Keyword-based analysis (no external ML dependencies)
  - Analyzes news titles and descriptions
  - Returns sentiment score and classification
  - Expandable keyword lists for customization

### Historical Data
- Fetches daily aggregates (OHLCV)
- Configurable date ranges (30 days default)
- Displays in pandas DataFrame format
- Includes volume data

### Web Interface (Dash)
- Built with Dash (Plotly) - industry standard for Python web apps
- Interactive Plotly charts with zoom, pan, and hover
- Responsive design that works on desktop and tablet
- Real-time updates without page refresh
- Professional styling with color-coded components
- Dark mode support
- Download charts as PNG images

---

## Limitations & Notes

### Polygon.io
- **Rate Limits**: Free tier has rate limits; respect API guidelines
- **WebSocket**: Real-time streaming requires active WebSocket connection
- **News**: News availability depends on Polygon.io's coverage
- **Sentiment**: Keyword-based analysis (basic)

### Alpha Vantage
- **Rate Limits**: 
  - Free tier: 25 calls/day, 5 calls/minute
  - Script enforces minimum 12-second intervals
  - Consider upgrading for higher limits
- **WebSocket**: Not available in free tier; uses polling instead
- **News**: NEWS_SENTIMENT endpoint provides AI-powered sentiment scores
- **Crypto**: Supports major crypto pairs (BTC, ETH, etc.)
- **Real-time**: Uses polling (GLOBAL_QUOTE for stocks, CRYPTO_INTRADAY for crypto)

### xAI Grok
- **Latency**: Adds ~1-2 seconds per analysis (TTFT in fast mode)
- **Costs**: Per-token pricing; check x.ai/pricing for current rates
- **Rate Limits**: Based on your xAI tier; free tier has limits
- **Reasoning Traces**: Available for transparency; can be verbose

### General
- **Crypto Pairs**: Defaults to USD pairs; extend code for other currencies
- **Data Source**: Choose based on your needs (Polygon for real-time, Alpha Vantage for free tier with sentiment)
- **AI Enhancement**: Grok provides advanced analysis but is optional; falls back gracefully if unavailable

---

## Error Handling

The script includes comprehensive error handling for:
- API connection failures
- Invalid ticker symbols
- Missing data
- WebSocket disconnections
- Network timeouts
- Rate limit violations
- Invalid API keys
- Missing dependencies

---

## Compliance (2025 Standards)

- No persistent data storage (privacy-compliant)
- Environment variables for API keys (secure)
- Secure WebSocket connections (wss://)
- Minimal data retention
- Open-source code for transparency
- No tracking or analytics

---

## Troubleshooting

**"Error fetching historical data"**
- Check your API key is valid
- Verify ticker symbol is correct
- Ensure you have API credits remaining
- Check your internet connection

**"No real-time updates"**
- Verify WebSocket access in your API plan (Polygon only)
- Check network connectivity
- Ensure ticker is actively traded
- Alpha Vantage uses polling, not WebSocket

**"No news available"**
- Some tickers may have limited news coverage
- Try a more popular ticker (e.g., AAPL, BTC-USD)
- Check if your API tier includes news access

**"Dashboard won't load"**
- Ensure port 8050 is not in use by another application
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.8 or higher: `python --version`
- Check for error messages in the terminal

**"Charts not displaying"**
- Check browser console for JavaScript errors
- Ensure internet connection is active (for Plotly CDN)
- Try refreshing the page
- Clear browser cache

**"Alpha Vantage rate limit"**
- You've exceeded the 5 calls/minute limit
- Wait 12 seconds between calls
- Consider upgrading to a paid Alpha Vantage plan
- Or switch to Polygon for higher rate limits

**"Alpha Vantage API error"**
- Check your API key is valid
- Verify ticker symbol is correct
- Ensure you haven't exceeded daily limit (25 calls/day free tier)

**"xAI Grok error"**
- Verify your xAI API key is valid
- Check your xAI account has available credits
- Ensure xai-sdk is installed: `pip install xai-sdk`
- Script will fall back to basic sentiment if Grok fails

**"Module not found" errors**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`
- Check Python version compatibility

---

## Contributing

Contributions are welcome! Areas for improvement:
- Additional technical indicators
- More data sources
- Export functionality (CSV, PNG)
- Multi-ticker monitoring
- Price alerts and notifications
- Mobile app version
- Additional chart types
- Performance optimizations

---

## License

See LICENSE file for details.

---

## Support

For issues with:
- **Polygon.io API**: Contact [Massive support](https://massive.com)
- **Alpha Vantage API**: Contact [Alpha Vantage support](https://www.alphavantage.co/support/)
- **xAI Grok API**: Contact [xAI support](https://x.ai/support) or check [x.ai/api](https://x.ai/api)
- **This Project**: Open an issue in the [GitHub repository](https://github.com/seanebones-lang/stockbro)

---

## Acknowledgments

- **Polygon.io (Massive)**: Market data and WebSocket streaming
- **Alpha Vantage**: Free-tier financial data and sentiment analysis
- **xAI**: Grok 4.1 Fast reasoning for advanced sentiment analysis
- **Dash (Plotly)**: Web framework and interactive visualizations
- **Pandas & NumPy**: Data processing and analysis

---

**Built with ❤️ for financial data enthusiasts**

*Empowering traders, investors, and researchers with accessible, professional-grade financial analysis tools.*
