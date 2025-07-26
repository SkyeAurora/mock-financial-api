import os
import json
import random
from datetime import datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA", "META", "NVDA", "BABA", "NFLX", "INTC"]  # 可自行扩展

today = datetime.now().strftime("%Y-%m-%d")

for symbol in symbols:
    open_price = round(random.uniform(100, 300), 4)
    high_price = round(open_price + random.uniform(0, 10), 4)
    low_price = round(open_price - random.uniform(0, 10), 4)
    price = round(random.uniform(low_price, high_price), 4)
    prev_close = round(open_price + random.uniform(-5, 5), 4)
    change = round(price - prev_close, 4)
    change_percent = f"{(change / prev_close * 100):.4f}%"
    volume = random.randint(1000000, 100000000)

    data = {
        "Global Quote": {
            "01. symbol": symbol,
            "02. open": f"{open_price:.4f}",
            "03. high": f"{high_price:.4f}",
            "04. low": f"{low_price:.4f}",
            "05. price": f"{price:.4f}",
            "06. volume": str(volume),
            "07. latest trading day": today,
            "08. previous close": f"{prev_close:.4f}",
            "09. change": f"{change:.4f}",
            "10. change percent": change_percent
        }
    }

    filename = f"{symbol}_NEWS_SENTIMENT_STOCKS.json"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Mock stock data generated.")
