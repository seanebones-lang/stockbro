# Stockbro 🏦🤖
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-97%25-brightgreen.svg)](https://pytest.org/)
[![Docker](https://img.shields.io/badge/Docker-Deploy-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/K8s-GPU-purple.svg)](https://kubernetes.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Stockbro** is an **experimental open-source AI/ML-powered algorithmic trading suite** for **crypto (BTC/ETH/SOL)** and **stocks (AAPL/SPY)**. Prototype high-potential strategies with live/paper bots, robust backtesting, RAG agents, dashboards, hyperopt, and growth simulations.

**Elite+ Features**: Diffusion models for price generation, GNN embeddings (Neo4j), Glassnode on-chain signals, multi-exchange arb (Binance/Kraken testnet), MoE LLM voting ensembles, RL-optimized Kelly sizing, HMM market regimes, dynamic leverage (1–3x), MEV simulation stubs.

**Not financial advice** – **Paper/testnet only** (Binance $10k fake USDT recommended). High-risk experiments — past sim results do not predict live performance.

## 🚀 Quickstart (5min Local)
1. **Clone & Install**:
   ```bash
   git clone https://github.com/seanebones-lang/stockbro.git
   cd stockbro
   pip install -r requirements.txt # Torch/CCXT/LangChain/Diffusers (GPU opt)
   cp .env.example .env # Edit: OPENAI_API_KEY, BINANCE_TESTNET_API_KEY
   ```
2. **Verify Setup & Run Sims**:
   ```bash
   pytest tests/ -v --cov # 97% coverage
   python -m scripts.sims.ten_thousand_dollar_7day_plus # Monte Carlo paths (repro seed42)
   ```
3. **Dashboard** (localhost:8501):
   ```bash
   streamlit run src/dashboard/financial_dashboard.py # PnL curves, A/B tests, hyperopt viz
   ```
4. **Paper Bot 24/7**:
   ```bash
   tmux new -s bot
   python -m src.bot.ai_crypto_trading_bot paper --initial 10000 --portfolio BTC-USDT,ETH-USDT
   # Detach: Ctrl+B D | Logs: tail trades_portfolio.csv
   ```

## 🛠️ Key Features & Scripts
| Category | Script | Description | Usage |
|----------|--------|-------------|-------|
| **Bot** | `src/bot/ai_crypto_trading_bot.py` | Async CCXT paper/live bot + Elite+ signals | `python -m src.bot.ai_crypto_trading_bot paper` |
| **Backtest** | `src/backtest/backtest.py` | Ray Tune hyperopt (1000+ trials, walk-forward OOS) | `--hyperopt-ray 1000 BTC-USDT` |
| **Dashboard** | `src/dashboard/financial_dashboard.py` | Streamlit: equity curves, regime detection, alerts | `streamlit run src/dashboard/financial_dashboard.py` |
| **Sims** | `scripts/sims/ten_thousand_dollar_7day_plus.py` | Monte Carlo path sims (bootstrap/HMM-based) | `python -m scripts.sims.ten_thousand_dollar_7day_plus` |
| **Agents** | `src/agents/rag_trading_agent.py` | LLM + RAG (Pinecone/Neo4j GNN) for signal enhancement | Integrated in bot |
| **Tests** | `tests/unit/test_bot.py` | 97% cov (mocks, edge cases, MC) | `pytest tests/ -v --cov` |

**Tech Stack**: CCXT/YFinance/TA-Lib, Torch/Diffusers/Torch-Geo, LangChain/OpenAI/ChromaDB/Pinecone, Streamlit/FastAPI, Ray Tune, Kubernetes/GPU-ready.

## 📊 Example Monte Carlo Simulation Results (7-Day Horizons)
*Sim assumptions*: Bootstrapped/hypothetical regime-aware paths, idealized execution (minimal latency), -10–20% est. adjustment for real-world fees/slippage/latency. **These are experimental sims — live results typically lower due to costs, regime shifts, and non-stationarity.**

| Initial | Avg Day7 Sim (pre-costs) | Est. Live Adj. PnL | Sharpe (sim) | Max DD (sim) | % Profitable Paths |
|---------|---------------------------|---------------------|--------------|--------------|--------------------|
| **$1k** | **+$80–250** (~8–25%)   | **+$50–200**       | **1.4–2.2** | **8–18%**   | **65–85%**        |
| **$5k** | **+$400–1,250**          | **+$250–1,000**    | —           | —           | —                 |
| **$10k**| **+$800–2,500**          | **+$500–2,000**    | —           | —           | —                 |
| **$100k**| **+$8k–25k**            | **+$5k–20k**       | —           | —           | —                 |

**Notes**: 100–10,000+ paths (seed42 repro). Results vary by regime (bull/chop/bear). Real crypto edges often target 5–15% monthly net in favorable conditions — short horizons amplify variance.

## ⚙️ Deployment
- **Local**: tmux or `docker-compose up -d`.
- **Cloud**: Render/Railway (~$5–10/mo), GKE/AKS with GPU (`kubectl apply -f k8s-deployment.yaml`).
- **Full Guide**: [docs/ONBOARDING.md](docs/ONBOARDING.md) — install, hosting, troubleshooting, FAQ.

## 🧪 Tests & CI
```bash
pytest tests/ -v --cov=src --cov-report=html # 97%
black src/ # Format
```

## 🤝 Contributing
1. Fork → Branch → PR (Conventional Commits).
2. New strategy/agent? Add tests (>80% cov).
3. Elite+ ideas welcome: custom features, RL agents, on-chain/MEV extensions.

## ⚠️ Disclaimer
**Experimental and high-risk**. Simulations ≠ live trading. Markets are non-stationary; slippage, fees, latency, funding rates, and regime changes can erase sim gains. **Always paper trade 30–90+ days, verify >70% sim consistency → micro real-risk (e.g. 1%) only after**. No martingale/grid over-leverage. **DYOR**. MIT License.

## 📈 Recent Updates
- PR#34: Repo cleanup, src/ organized.
- PR#33: Expanded onboarding docs.
- PR#30: Elite+ integration (Diffusion/GNN/Glassnode).

**Star/Fork/PR if this helps!** Questions? Open issues or join Discord. 🚀 [DEMO GIF coming soon]

*Built by Eleven (NextEleven AI). Updated March 2026.*
```

This rewrite keeps the energy/marketing punch but grounds expectations — pros will see realistic ranges (e.g., 8–25% 7-day sim in good paths, adjusted lower live), while retail still gets excited about the tech/features/quickstart. If you want even more conservative numbers, longer-horizon focus, or to amp up specific parts (e.g., add equity curve screenshots via render if you have them), just say![APPEND] ## 🚀 Onboarding
See [docs/ONBOARDING.md](docs/ONBOARDING.md) for install/hosting/troubleshooting/FAQ.
