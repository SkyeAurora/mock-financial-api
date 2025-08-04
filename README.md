# 📈 Mock Financial API Server 模拟金融数据接口服务

一个用于模拟金融数据 API 的轻量级服务端项目，支持根据请求参数返回预设的 JSON 数据，适用于前端联调、回测测试、接口模拟等场景。

A lightweight server-side project for simulating financial data APIs. It returns predefined JSON responses based on query parameters, ideal for frontend integration, strategy backtesting, and development testing.

---

## 🚀 项目特点 Features

- 支持模拟 Alpha Vantage 风格的行情接口
- 请求参数映射到本地 JSON 文件
- 可自由添加、管理模拟数据
- 可扩展多个接口模块：行情 / 指标 / 新闻 等
- 支持 Flask 本地运行，部署简单

---

## ⚙️ 快速开始 Quick Start

### 📌 安装依赖

建议使用虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

### 🚀 启动服务 Start Server

```bash
python server.py
```

默认运行在端口 5555，可访问：`http://localhost:5555`

---

## 📊 API 接口说明 API Endpoints

### 🏗️ 路由映射规则 Route Mapping Rules

本项目通过请求参数自动映射到对应的本地 JSON 文件，无需手动配置路由。

This project automatically maps request parameters to corresponding local JSON files without manual route configuration.

#### 📈 股票数据接口 Stock Data API
**端点 Endpoint**: `/stocks`

**映射规则 Mapping Rule**: `{symbol}_{function}.json`

**请求参数 Parameters**:
- `function`: 数据类型 (例如: `TIME_SERIES_DAILY`, `GLOBAL_QUOTE`, `NEWS_SENTIMENT`)
- `symbol`: 股票代码 (例如: `AAPL`, `MSFT`, `GOOGL`)
- `tickers`: 批量查询时使用

**示例请求 Example Request**:
```bash
# 获取苹果股票的日线数据
GET /stocks?function=TIME_SERIES_DAILY&symbol=AAPL

# 获取微软股票的实时报价
GET /stocks?function=GLOBAL_QUOTE&symbol=MSFT

# 获取涨跌幅排行榜
GET /stocks?function=TOP_GAINERS_LOSERS
```

#### 🪙 加密货币接口 Cryptocurrency API
**端点 Endpoint**: `/cryptos`

**映射规则 Mapping Rule**: `{symbol}_{function}.json`

**请求参数 Parameters**:
- `function`: 数据类型 (例如: `CRYPTO_LAST_PRICE`)
- `symbol`: 加密货币代码 (例如: `BTC`, `ETH`, `ADA`)

**示例请求 Example Request**:
```bash
# 获取比特币最新价格
GET /cryptos?function=CRYPTO_LAST_PRICE&symbol=BTC

# 获取以太坊最新价格
GET /cryptos?function=CRYPTO_LAST_PRICE&symbol=ETH
```

#### 🛢️ 大宗商品接口 Commodities API
**端点 Endpoint**: `/commodities`

**映射规则 Mapping Rule**: `{function}_{interval}.json`

**请求参数 Parameters**:
- `function`: 商品类型 (例如: `WTI`, `BRENT`, `GOLD`, `COPPER`)
- `interval`: 时间间隔 (例如: `daily`, `weekly`, `monthly`, `quarterly`, `annual`)

**示例请求 Example Request**:
```bash
# 获取 WTI 原油日线数据
GET /commodities?function=WTI&interval=daily

# 获取黄金周线数据
GET /commodities?function=GOLD&interval=weekly
```

---

## 🤖 自动数据生成 Automated Data Generation

项目提供了多个脚本来自动从 Alpha Vantage API 获取真实金融数据并保存为本地 JSON 文件。

The project provides several scripts to automatically fetch real financial data from Alpha Vantage API and save as local JSON files.

### 📋 数据生成脚本 Data Generation Scripts

#### 1️⃣ 股票数据生成 Stock Data Generation

**`auto_generate_mock_stocks.py`** - 批量生成股票时间序列数据
- 支持的函数类型: `TIME_SERIES_INTRADAY`, `TIME_SERIES_DAILY`, `TIME_SERIES_WEEKLY` 等
- 支持的股票: AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA 等 20+ 支主要股票
- 自动保存到: `data/stocks/` 目录

**`generate_mock_stocks.py`** - 生成特定类型股票数据
- 主要用于生成 `GLOBAL_QUOTE` 类型数据
- 可自定义股票列表和数据类型

#### 2️⃣ 大宗商品数据生成 Commodities Data Generation

**`auto_generate_mock_data.py`** - 批量生成大宗商品数据
- 支持的商品: WTI, BRENT, NATURAL_GAS, COPPER, ALUMINUM, WHEAT, CORN, COTTON, COFFEE, SUGAR
- 支持的时间间隔: daily, weekly, monthly, quarterly, annual
- 自动保存到: `data/commodities/` 目录

### 🔧 使用数据生成脚本 Using Data Generation Scripts

```bash
# 生成股票数据
python auto_generate_mock_stocks.py

# 生成大宗商品数据
python auto_generate_mock_data.py

# 生成特定股票报价数据
python generate_mock_stocks.py
```

### ⚠️ 注意事项 Important Notes

1. **API 密钥**: 需要在脚本中配置有效的 Alpha Vantage API KEY
2. **请求限制**: 免费账户每分钟最多 5 次请求，脚本已自动处理限速 (15秒间隔)
3. **数据覆盖**: 重复运行脚本会覆盖现有数据文件
4. **网络连接**: 需要稳定的网络连接来获取数据
5. **API请求次数限制**： 可以通过切换VPN节点更新请求次数限制（仅限根据IP进行限制的API 比如Alpha Vantage API）

---

## 📁 数据文件结构 Data File Structure

```
data/
├── stocks/          # 股票数据 Stock Data
│   ├── AAPL_TIME_SERIES_DAILY.json
│   ├── MSFT_GLOBAL_QUOTE.json
│   └── ...
├── cryptos/         # 加密货币数据 Crypto Data
│   ├── BTC_CRYPTO_LAST_PRICE.json
│   ├── ETH_CRYPTO_LAST_PRICE.json
│   └── ...
└── commodities/     # 大宗商品数据 Commodities Data
    ├── WTI_daily.json
    ├── GOLD_weekly.json
    └── ...
```

---

## 🎯 使用场景 Use Cases

- **前端开发**: 模拟真实 API 响应进行前端联调
- **策略回测**: 提供历史数据进行量化策略测试
- **接口测试**: 在无网络环境下进行接口功能测试
- **演示展示**: 稳定的模拟数据用于产品演示
- **开发调试**: 避免频繁调用外部 API 的限制和成本

- **Frontend Development**: Mock real API responses for frontend integration
- **Strategy Backtesting**: Provide historical data for quantitative strategy testing
- **API Testing**: Test interface functionality in offline environments
- **Demo Presentations**: Stable mock data for product demonstrations
- **Development & Debugging**: Avoid external API rate limits and costs

---

## 🚀 启动服务 Start Server

```bash
python server.py
```

默认运行在端口 5555，服务启动后可通过浏览器访问：`http://localhost:5555`

Server runs on port 5555 by default, access via: `http://localhost:5555`

---

## 🛠️ 扩展开发 Extension Development

### 添加新的数据类型 Adding New Data Types

1. 在相应目录下添加 JSON 数据文件
2. 按照命名规范：`{symbol}_{function}.json` 或 `{function}_{interval}.json`
3. 服务器会自动识别并提供 API 访问

Add JSON data files in the corresponding directory following the naming convention, and the server will automatically recognize and provide API access.

### 自定义数据生成 Custom Data Generation

可以参考现有脚本创建自定义的数据生成器，只需：
1. 配置 API 密钥和请求参数
2. 设置数据保存路径和文件名
3. 添加合适的限速和错误处理

You can create custom data generators by referencing existing scripts.

---

## 📝 技术栈 Tech Stack

- **Backend**: Python 3.x + Flask
- **Data Source**: Alpha Vantage API
- **Data Format**: JSON
- **HTTP Client**: requests

---

## 🤝 贡献 Contributing

欢迎提交 Issue 和 Pull Request 来改进项目！

Welcome to submit Issues and Pull Requests to improve the project!

---
