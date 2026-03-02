import subprocess
symbols = ['BTC-USD', 'ETH-USD', 'SOL-USD']
results = {}
for sym in symbols:
    result = subprocess.run(['python', 'backtest.py', '--symbol', sym, '--days', '180'], capture_output=True, text=True)
    print(result.stdout)
    # Parse for metrics
print('Summary: Avg Sharpe', sum(...)/3)