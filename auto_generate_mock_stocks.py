import os
import json
import time
import requests
from datetime import datetime

# 设置保存目录
DATA_DIR = os.path.join("data", "stocks")
os.makedirs(DATA_DIR, exist_ok=True)

#functions = ["TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_WEEKLY_ADJUSTED", "TIME_SERIES_MONTHLY", "TIME_SERIES_MONTHLY_ADJUSTED"]
functions = ["TIME_SERIES_INTRADAY"]
symbols = [
  "AAPL",     # Apple Inc.
  "MSFT",     # Microsoft Corporation
  "GOOGL",    # Alphabet Inc. (Google)
  "AMZN",     # Amazon.com, Inc.
  "META",     # Meta Platforms Inc. (Facebook)
  "TSLA",     # Tesla Inc.
  "NVDA",     # NVIDIA Corporation
  "BRK-B",    # Berkshire Hathaway Inc. Class B
  "JPM",      # JPMorgan Chase & Co.
  "JNJ",      # Johnson & Johnson
  "V",        # Visa Inc.
  "WMT",      # Walmart Inc.
  "UNH",      # UnitedHealth Group
  "HD",       # Home Depot
  "MA",       # Mastercard Inc.
  "PG",       # Procter & Gamble
  "DIS",      # Walt Disney Company
  "PEP",      # PepsiCo, Inc.
  "KO",       # Coca-Cola Company
  "BAC"       # Bank of America
]
API_KEY = "ODQ7Q5K7RG72G8SW"
BASE_URL = "https://www.alphavantage.co/query"
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&outputsize=full&apikey=ODQ7Q5K7RG72G8SW
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for symbol in symbols:
    for function in functions:
        # 构造请求参数
        params = {
            "function": function,
            "symbol": symbol,
            "interval": "5min",  # 5分钟间隔
            "outputsize": "full",  # 获取完整数据
            "apikey": API_KEY
        }

        try:
            print(f"📡 Fetching {function} - {symbol} ...")
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # 检查是否是合法的响应
            if not data or "Error Message" in data or "Note" in data:
                print(f"⚠️ Failed to fetch {function} ({symbol}) - API message: {data.get('Note') or data.get('Error Message')}")
            else:
                # 保存为 JSON 文件
                filename = f"{symbol}_{function}.json"
                filepath = os.path.join(DATA_DIR, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"✅ Saved {filename}")

        except Exception as e:
            print(f"❌ Error fetching {function} ({symbol}): {e}")

        # 限速处理：Alpha Vantage 免费用户为每分钟最多 5 次请求
        time.sleep(15)  # 建议 sleep 15 秒以规避限速

print("🎉 数据抓取完成，文件保存在 /data/commodities/")
