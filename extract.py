import requests
import pandas as pd


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]]

    return df
