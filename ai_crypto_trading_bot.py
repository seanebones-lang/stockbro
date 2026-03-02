#!/usr/bin/env python3
"""AI Crypto/Stock Trading Bot: ML (XGBoost) + RAG + Graph features for predictions."""

import os
import argparse
import logging
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import yfinance as yf
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
    # Import prior components
    from rag_trading_agent import query_rag, TradingSignal
from knowledge_graph import StockbroGraph
except ImportError as e:
    logger.error(f'Missing dep: {e}. pip install -r requirements.txt')
    exit(1)

MODEL_PATH = 'stockbro_xgb_model.json'
SCALER_PATH = 'stockbro_scaler.pkl'  # Note: use joblib for scaler save/load

class TradingBot:
    def __init__(self):
        self.graph = StockbroGraph()
        self.model = None
        self.scaler = StandardScaler()

    def fetch_features(self, ticker: str, period: str = '6mo') -> pd.DataFrame:
        """OHLCV + tech indicators + Graph ML feats + RAG sentiment."""
        # yfinance OHLCV
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        df['Return'] = df['Close'].pct_change()
        df['MA_5'] = df['Close'].rolling(5).mean()
        df['RSI'] = self._rsi(df['Close'])
        df['Volatility'] = df['Return'].rolling(20).std()

        # Graph feats
        graph_feats = self.graph.get_ml_features([ticker])
        df['pagerank'] = graph_feats[ticker]['pagerank']
        df['degree'] = graph_feats[ticker]['degree']

        # RAG sentiment (sample recent query)
        rag_signal = query_rag(f'{ticker} trading outlook', k=3)
        df['rag_confidence'] = rag_signal.confidence / 100.0  # Latest for all rows approx

        df.dropna(inplace=True)
        return df

    def _rsi(self, prices: pd.Series, window: int = 14) -> pd.Series:
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def prepare_labels(self, df: pd.DataFrame) -> pd.DataFrame:
        """Label: 1=Bull (next ret>1%), 0=Bear (< -1%), 2=Hold."""
        df['Next_Return'] = df['Return'].shift(-1)
        df['Label'] = np.where(df['Next_Return'] > 0.01, 1,
                               np.where(df['Next_Return'] < -0.01, 0, 2))
        df.dropna(inplace=True)
        return df

    def train(self, ticker: str):
        """Train XGBoost on features/labels."""
        df = self.fetch_features(ticker)
        df = self.prepare_labels(df)

        features = ['Return', 'MA_5', 'RSI', 'Volatility', 'pagerank', 'degree', 'rag_confidence']
        X = df[features]
        y = df['Label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Train
        self.model = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
        self.model.fit(X_train_scaled, y_train)

        # Eval
        preds = self.model.predict(X_test_scaled)
        acc = accuracy_score(y_test, preds)
        logger.info(f'Accuracy: {acc:.2f}\n{classification_report(y_test, preds)}')

        # Save
        self.model.save_model(MODEL_PATH)
        import joblib
        joblib.dump(self.scaler, SCALER_PATH)
        logger.info('Model saved')

    def predict(self, ticker: str) -> Dict[str, Any]:
        """Predict signal for ticker."""
        if self.model is None:
            import joblib
            self.model = xgb.XGBClassifier()
            self.model.load_model(MODEL_PATH)
            self.scaler = joblib.load(SCALER_PATH)

        df = self.fetch_features(ticker, period='1mo')
        latest = df.iloc[-1:]
        features = ['Return', 'MA_5', 'RSI', 'Volatility', 'pagerank', 'degree', 'rag_confidence']
        X_latest = self.scaler.transform(latest[features])

        pred = self.model.predict(X_latest)[0]
        probs = self.model.predict_proba(X_latest)[0]

        signals = {0: 'SELL', 1: 'BUY', 2: 'HOLD'}
        return {
            'ticker': ticker,
            'prediction': signals[pred],
            'probs': dict(zip(signals.values(), probs)),
            'confidence': max(probs) * 100
        }

    def backtest(self, ticker: str, period: str = '1y'):
        """Simple backtest: buy/hold strategy vs ML signals."""
        df = self.fetch_features(ticker, period)
        df = self.prepare_labels(df)
        # Load model, simulate trades...
        logger.info('Backtest stub: implement PnL calc')
        print(df.tail())

if __name__ == '__main__':
    bot = TradingBot()
    parser = argparse.ArgumentParser(description='AI Trading Bot')
    parser.add_argument('mode', choices=['train', 'predict', 'backtest'], help='Mode')
    parser.add_argument('ticker', help='Ticker e.g. BTC-USD')
    parser.add_argument('--period', default='6mo', help='Data period')

    args = parser.parse_args()

    if args.mode == 'train':
        bot.train(args.ticker)
    elif args.mode == 'predict':
        signal = bot.predict(args.ticker)
        print(signal)
    elif args.mode == 'backtest':
        bot.backtest(args.ticker, args.period)

    bot.graph.close()
    logger.info('Bot session complete')
