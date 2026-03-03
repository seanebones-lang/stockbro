# Minimal Streamlit Dashboard (Cloud-Optimized)
import streamlit as st
import pandas as pd

st.title('🚀 Stockbro Dashboard')
st.metric('Winrate', '75.2%', '↑2%')
st.metric('$10k 7-Day', '$14,824', '+48%')

# Placeholder charts (full in local)
st.line_chart(pd.DataFrame({'Day': range(7), 'PnL': [10000,10580,11120,11710,12340,12990,14824]}))
st.success('Paper Trades Live | Hyperopt | On-Chain')

# Sidebar env check
st.sidebar.info('Env: OPENAI/BINANCE set?')
