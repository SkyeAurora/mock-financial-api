import os
import json
import random
from datetime import datetime

# 设置目录
DATA_DIR = os.path.join("data", "commodities")
os.makedirs(DATA_DIR, exist_ok=True)

functions = ["WTI","BRENT","NATURAL_GAS","COPPER","ALUMINUM","WHEAT","CORN","COTTON","COFFEE","SUGAR"]
intervals = ["monthly","quarterly","annual"]


today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for interval in intervals:
    # 构造数据
    data = { }

    # 保存为 JSON 文件
    filename = f"{functions}_{interval}.json"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Mock crypto data with names generated in /data/cryptos/")
