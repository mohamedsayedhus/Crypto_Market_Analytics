import pandas as pd
from datetime import datetime


def transform_crypto_data(df):
    df["load_date"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    # KPIs
    df["market_cap_rank"] = df["market_cap"].rank(ascending=False)
    df["volume_to_market_cap"] = df["total_volume"] / df["market_cap"]

    # Flags
    df["trend"] = df["price_change_percentage_24h"].apply(
        lambda x: "Bullish" if x > 0 else "Bearish"
    )

    return df
