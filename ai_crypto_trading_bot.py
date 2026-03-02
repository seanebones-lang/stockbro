import os
import time
import threading
import pandas as pd
import numpy as np
import talib
from datetime import datetime
import ccxt
from dotenv import load_dotenv
import json
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
# RAG/Graph
from rag_trading_agent import get_rag_signal
from knowledge_graph import get_graph_feats
load_dotenv()

class AITradingBot:
    def __init__(self, symbol='BTC/USDT', mode='paper'):
        self.symbol = symbol
        self.mode = mode
        self.balance = 10000
        self.position = 0
        self.entry_price = 0
        self.price_history = []
        self.ml_model = XGBClassifier()
        self.scaler = StandardScaler()
        self._setup_exchange()

    def _generate_signal(self):
        if len(self.price_history) < 50:
            return 'HOLD'
        closes = np.array([p for p in self.price_history[-50:]])
        rsi = talib.RSI(closes)[-1]
        ta_str = f'RSI:{rsi:.1f} oversold:{rsi<35}'
        try:
            rag_sig, rag_conf = get_rag_signal(ta_str, self.symbol)
            graph = get_graph_feats(self.symbol)
            feats = np.array([[rsi, graph.get('degree', 0), graph.get('avg_impact', 0)]])
            feats = self.scaler.transform(feats)
            ml_prob = self.ml_model.predict_proba(feats)[0][1]
            if rag_conf > 0.7 and ml_prob > 0.6:
                return rag_sig
        except:
            pass
        return 'HOLD'  # Safe fallback

    # Full _setup_exchange, _fetch_price, _execute, start/stop, get_status as prior real bot

if __name__ == '__main__':
    bot = AITradingBot()
    bot.start()