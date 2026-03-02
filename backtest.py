import os
import argparse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from polygon import RESTClient
import talib

class Backtester:
    def __init__(self, symbol, days=365, initial_balance=10000, fee=0.001):
        self.symbol = symbol.replace('-', '/')
        self.initial_balance = initial_balance
        self.fee = fee
        self.data = self._fetch_data(days)
        self.trades = []

    def _fetch_data(self, days):
        api_key = os.getenv('POLYGON_API_KEY')
        if not api_key:
            raise ValueError('Set POLYGON_API_KEY')
        client = RESTClient(api_key)
        end = datetime.now()
        start = end - timedelta(days=days)
        aggs = client.get_aggs(self.symbol, 1, 'minute', start, end, limit=50000)
        df = pd.DataFrame([a.__dict__ for a in aggs])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('timestamp')[['close', 'volume']].sort_index()
        df['returns'] = df['close'].pct_change()
        return df

    def run(self):
        balance = self.initial_balance
        position = 0
        entry_price = 0
        equity_curve = [balance]
        for i in range(100, len(self.data)):
            row = self.data.iloc[i]
            closes = self.data['close'].iloc[max(0, i-100):i+1].values
            volumes = self.data['volume'].iloc[max(0, i-100):i+1].values
            rsi = talib.RSI(closes)[-1]
            stoch_k = talib.STOCH(closes)[0][-1]
            adx = talib.ADX(closes)[-1]
            price = row['close']
            signal = 'HOLD'
            if position == 0 and rsi < 32 and stoch_k < 20 and adx > 25:
                signal = 'BUY'
            elif position > 0:
                pnl = (price - entry_price) / entry_price
                if pnl >= 0.015 or pnl <= -0.01:
                    signal = 'SELL'
            if signal == 'BUY':
                stake = balance * 0.1
                qty = stake / price
                cost = qty * price * (1 + self.fee)
                if balance >= cost:
                    position = qty
                    balance -= cost
                    entry_price = price
            elif signal == 'SELL' and position > 0:
                proceeds = position * price * (1 - self.fee)
                pnl_pct = (price - entry_price) / entry_price
                balance += proceeds
                self.trades.append(pnl_pct)
                position = 0
            equity_curve.append(balance + position * price)
        final = equity_curve[-1]
        returns = pd.Series(equity_curve).pct_change().dropna()
        sharpe = returns.mean() / returns.std() * np.sqrt(252 * 1440) if returns.std() > 0 else 0
        mdd = (pd.Series(equity_curve).cummax() - pd.Series(equity_curve)).max() / pd.Series(equity_curve).cummax().max()
        winrate = sum(p > 0 for p in self.trades) / len(self.trades) * 100 if self.trades else 0
        print(f'{self.symbol}: Final ${final:.2f} | PnL {((final/self.initial_balance)-1)*100:+.1f}% | Sharpe {sharpe:.2f} | MDD {mdd*100:.1f}% | Winrate {winrate:.1f}% | Trades {len(self.trades)}')
        return {'pnl': ((final/self.initial_balance)-1)*100, 'sharpe': sharpe, 'mdd': mdd*100, 'winrate': winrate}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', default='BTC-USD')
    parser.add_argument('--days', type=int, default=365)
    args = parser.parse_args()
    bt = Backtester(args.symbol, args.days)
    bt.run()