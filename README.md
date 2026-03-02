# StockBro: Real-Time Financial Dashboard + AI Crypto Bot

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` → `.env`, add keys.
3. `python financial_dashboard.py` → http://127.0.0.1:8050

## AI Trading Bot 🚨
- **Simulation** (default): Biased demo profits (RSI/MA/Prophet/Grok).
- **Paper/Live**: Binance testnet keys → real orders (small stake!).
- Buy: RSI<32 + bull signals. Sell: 1.5% profit/-1% stop.
- **NO daily doubling guarantee** - risky! Start sim.

Status/charts update live. Stop anytime.

## Disclaimer
Markets volatile. Past/demo != future. Use at own risk.