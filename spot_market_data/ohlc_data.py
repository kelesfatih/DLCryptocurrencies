import requests
import pandas as pd
import datetime
from spot_market_data import server_time

# Get today's date
today = server_time.get_server_time()
# Calculate 720 days ago
days_ago = today - datetime.timedelta(days=720)


def get_ohlc_data(pair, interval, since=days_ago):
    # URL of API
    url = f"https://api.kraken.com/0/public/OHLC?"
    # Requesting data from API
    resp = requests.get(url,
                        params={
                            "pair": pair,
                            "interval": interval,
                            "since": str(int(pd.Timestamp(since).timestamp()))
                        })
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    data = resp.json()
    df = pd.DataFrame(data["result"][pair],
                      columns=["CloseTime", "OpenPrice", "HighPrice", "LowPrice",
                               "ClosePrice", "VWAP", "Volume", "Count"])
    # Converting timestamp to datetime
    df["CloseTime"] = pd.to_datetime(df["CloseTime"], unit="s")
    # Setting index to CloseTime
    df.set_index("CloseTime", inplace=True)
    df = df.apply(pd.to_numeric, errors="coerce")
    return df


# Testing the function
if __name__ == "__main__":
    print(get_ohlc_data(pair="BTC/USDT", interval=1440))
