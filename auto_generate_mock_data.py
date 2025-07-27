import os
import json
import time
import requests
from datetime import datetime

# 设置保存目录
DATA_DIR = os.path.join("data", "commodities")
os.makedirs(DATA_DIR, exist_ok=True)

functions = ["WTI", "BRENT", "NATURAL_GAS", "COPPER", "ALUMINUM", "WHEAT", "CORN", "COTTON", "COFFEE", "SUGAR"]
intervals = ["daily", "weekly"]
API_KEY = "ODQ7Q5K7RG72G8SW"
BASE_URL = "https://www.alphavantage.co/query"

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for function in functions:
    for interval in intervals:
        # 构造请求参数
        params = {
            "function": function,
            "interval": interval,
            "apikey": API_KEY
        }

        try:
            print(f"📡 Fetching {function} - {interval} ...")
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # 检查是否是合法的响应
            if not data or "Error Message" in data or "Note" in data:
                print(f"⚠️ Failed to fetch {function} ({interval}) - API message: {data.get('Note') or data.get('Error Message')}")
            else:
                # 保存为 JSON 文件
                filename = f"{function}_{interval}.json"
                filepath = os.path.join(DATA_DIR, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"✅ Saved {filename}")

        except Exception as e:
            print(f"❌ Error fetching {function} ({interval}): {e}")

        # 限速处理：Alpha Vantage 免费用户为每分钟最多 5 次请求
        time.sleep(15)  # 建议 sleep 15 秒以规避限速

print("🎉 数据抓取完成，文件保存在 /data/commodities/")
