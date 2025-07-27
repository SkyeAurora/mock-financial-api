from flask import Flask, request, jsonify, send_file, abort
import os
import json

app = Flask(__name__)

DATA_DIR = 'data'

@app.route('/stocks')
def queryStocks():
    function = request.args.get('function')
    symbol = request.args.get('symbol')
    tickers = request.args.get('tickers')
    # apikey = request.args.get('apikey')

    filename = f"{symbol}_{function}_STOCKS.json" if symbol else f"{tickers}_{function}_STOCKS.json"
    filepath = os.path.join(DATA_DIR + "/stocks", filename)

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        abort(404, description=f"No mock data found for {filename}")

@app.route('/cryptos')
def queryCryptos():
    function = request.args.get('function')
    symbol = request.args.get('symbol')
    tickers = request.args.get('tickers')
    # apikey = request.args.get('apikey')

    filename = f"{symbol}_{function}.json" if symbol else f"{tickers}_{function}.json"
    filepath = os.path.join(DATA_DIR + "/cryptos", filename)

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        abort(404, description=f"No mock data found for {filename}")

@app.route('/commodities')
def queryCommodities():
    function = request.args.get('function')
    interval = request.args.get('interval')
    # apikey = request.args.get('apikey')

    filename = f"{function}_{interval}.json"
    filepath = os.path.join(DATA_DIR + "/commodities", filename)

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        abort(404, description=f"No mock data found for {filename}")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
