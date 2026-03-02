import time
from ai_crypto_trading_bot import AITradingBot

bot = AITradingBot('BTC/USDT', 'simulation')
bot.start()
time.sleep(300)
bot.stop()
status = bot.get_status()
print(status)
print('✅ Test: Expect PnL >0%')