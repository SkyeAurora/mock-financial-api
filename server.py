from flask import Flask, request, jsonify, send_file, abort
import os
import json

app = Flask(__name__)

DATA_DIR = 'data'

@app.route('/stocks')
def query():
    function = request.args.get('function')
    symbol = request.args.get('symbol')
    tickers = request.args.get('tickers')
    # apikey = request.args.get('apikey')

    filename = f"{symbol}_{function}_STOCKS.json" if symbol else f"{tickers}_{function}_STOCKS.json"
    filepath = os.path.join(DATA_DIR, filename)

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        abort(404, description=f"No mock data found for {filename}")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
