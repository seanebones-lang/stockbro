#!/usr/bin/env python3
"""Backtesting for Stockbro ML Trading Bot: Simulate strategy PnL vs buy-hold."""

import os
import argparse
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Tuple, Dict

from ai_crypto_trading_bot import TradingBot
import yfinance as yf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Backtester:
    def __init__(self, ticker: str, period: str = '1y'):
        self.ticker = ticker
        self.period = period
        self.bot = TradingBot()

    def run(self) -> Tuple[Dict[str, float], pd.DataFrame]:
        """Full backtest: Fetch data, gen ML signals, simulate trades, compute metrics."""
        # Data
        stock = yf.Ticker(self.ticker)
        df = stock.history(period=self.period)
        df['Return'] = df['Close'].pct_change()

        # ML signals over time (approx daily predict)
        signals = []
        for date in df.index[20:]:  # Skip init
            # Mock historical predict (use current model approx)
            signal = self.bot.predict(self.ticker)
            signals.append({
                'date': date,
                'signal': signal['prediction'],
                'confidence': signal['confidence']
            })
        signals_df = pd.DataFrame(signals).set_index('date')

        df = df.join(signals_df, how='left')
        df['signal'].fillna('HOLD', inplace=True)

        # Strategy returns
        df['strategy_return'] = np.where(df['signal'] == 'BUY', df['Return'],
                                        np.where(df['signal'] == 'SELL', -df['Return'], 0))
        df['buy_hold_return'] = df['Return']

        df['strategy_cum'] = (1 + df['strategy_return']).cumprod()
        df['buy_hold_cum'] = (1 + df['buy_hold_return']).cumprod()

        # Metrics
        strategy_ret = df['strategy_return'].mean() * 252  # Annualized
        bh_ret = df['buy_hold_return'].mean() * 252
        strategy_sharpe = strategy_ret / df['strategy_return'].std() * np.sqrt(252)
        max_dd = (df['strategy_cum'] / df['strategy_cum'].cummax() - 1).min()

        metrics = {
            'Strategy Return (%)': strategy_ret * 100,
            'Buy & Hold Return (%)': bh_ret * 100,
            'Strategy Sharpe': strategy_sharpe,
            'Max Drawdown (%)': max_dd * 100,
            'Win Rate (%)': (df['strategy_return'] > 0).mean() * 100
        }

        logger.info('Backtest metrics: %s', metrics)
        self.plot(df, metrics)
        df.to_csv(f'{self.ticker}_backtest.csv')
        return metrics, df

    def plot(self, df: pd.DataFrame, metrics: Dict):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        df[['strategy_cum', 'buy_hold_cum']].plot(ax=ax1, title=f'{self.ticker} Backtest')
        ax1.legend(['ML Strategy', 'Buy & Hold'])
        df['strategy_return'].hist(ax=ax2, bins=50, alpha=0.7)
        ax2.set_title('Strategy Returns Distribution')
        fig.tight_layout()
        plt.savefig(f'{self.ticker}_backtest.png')
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backtest ML Trading Bot')
    parser.add_argument('ticker', help='Ticker')
    parser.add_argument('--period', default='1y', help='Period')
    args = parser.parse_args()

    bt = Backtester(args.ticker, args.period)
    metrics, df = bt.run()
    print(metrics)
    bt.bot.graph.close()
