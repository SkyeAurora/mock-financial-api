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

## 🚀 启动服务

python server.py
