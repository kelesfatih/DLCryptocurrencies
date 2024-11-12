import requests
import datetime
import numpy as np
import pandas as pd


def system_status():
    # URL of API
    url = "https://api.kraken.com/0/public/SystemStatus"
    # Requesting data from API
    resp = requests.get(url)
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    data = resp.json()
    # Extracting system status
    ss = data["result"]["status"]
    return ss


def server_time():
    # URL of API
    url = "https://api.kraken.com/0/public/Time"
    # Requesting data from API
    resp = requests.get(url)
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    data = resp.json()
    # Converting timestamp to datetime
    st = pd.to_datetime(data["result"]["unixtime"], unit="s")
    return st


def asset_pairs(option="all"):
    """
    Fetch asset pairs data from Kraken API and return based on the option:
    - "all" returns the full asset pairs data.
    - "names" returns an array of asset pair names.
    - "usdt" returns an array of USD-based asset pair names.
    """
    # URL of API
    url = "https://api.kraken.com/0/public/AssetPairs"
    # Requesting data from API
    resp = requests.get(url)
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    asset_pairs_list = resp.json()["result"]

    if option == "names":
        # Return only asset pair names
        return np.array([i['wsname'] for i in asset_pairs_list.values() if 'wsname' in i])
    elif option == "usdt":
        # Return only USD-based asset pair names
        return np.array([i['wsname'] for i in asset_pairs_list.values() if 'wsname' in i and 'USDT' in i['wsname']])
    else:
        # Return full asset pairs data
        return asset_pairs_list


def ohlc_data(pair, interval, since=None):
    # Set `since` to 720 days ago if not provided
    if since is None:
        since = server_time() - datetime.timedelta(days=720)
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

if __name__ == "__main__":
    print("main")