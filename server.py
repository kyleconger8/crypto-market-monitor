from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"

@app.route("/")
def home():
    return {"message": "Crypto MCP Server running"}

@app.route("/crypto", methods=["GET"])
def crypto():

    coins = request.args.get("coins", "bitcoin,ethereum,solana")

    params = {
        "ids": coins,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(COINGECKO_API, params=params)

    data = response.json()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
