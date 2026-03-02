from fastapi import FastAPI
app = FastAPI()
@app.get('/signal')
def signal(symbol: str):
    bot = AITradingBot(symbol)
    return bot.generate_signal_json()