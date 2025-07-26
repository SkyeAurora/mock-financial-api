import os
import json
import random
from datetime import datetime

# 设置目录
DATA_DIR = os.path.join("data", "cryptos")
os.makedirs(DATA_DIR, exist_ok=True)

# 加密货币符号和名称映射
crypto_info = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "BNB": "BNB",
    "SOL": "Solana",
    "XRP": "Ripple",
    "ADA": "Cardano",
    "DOGE": "Dogecoin",
    "AVAX": "Avalanche",
    "TRX": "TRON",
    "LINK": "Chainlink",
    "TON": "Toncoin",
    "DOT": "Polkadot",
    "MATIC": "Polygon",
    "SHIB": "Shiba Inu",
    "LTC": "Litecoin",
    "UNI": "Uniswap",
    "ETC": "Ethereum Classic",
    "XLM": "Stellar",
    "APT": "Aptos",
    "ICP": "Internet Computer"
}

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for symbol, name in crypto_info.items():
    # 模拟价格生成
    open_price = round(random.uniform(100, 300), 2)
    high_price = round(open_price + random.uniform(0, 10), 2)
    low_price = round(open_price - random.uniform(0, 10), 2)
    price = round(random.uniform(low_price, high_price), 2)
    prev_close = round(open_price + random.uniform(-5, 5), 2)
    change = round(price - prev_close, 2)
    change_percent = round((change / prev_close) * 100, 2)
    volume = random.randint(1_000_000, 100_000_000)

    # 构造数据
    data = {
        "code": symbol,
        "name": name,
        "timestamp": today,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "prev_close": prev_close,
        "change_percent": f"{change_percent}%",
        "volume": volume
    }

    # 保存为 JSON 文件
    filename = f"{symbol}_CRYPTO_LAST_PRICE.json"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Mock crypto data with names generated in /data/cryptos/")
