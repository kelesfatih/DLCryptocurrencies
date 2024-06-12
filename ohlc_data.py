import requests
import pandas as pd
import numpy as np


def get_ohlc_data(pair, interval, since):
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
    return df


# Testing the function
if __name__ == "__main__":
    asset_pairs_names_array = np.load('asset_pairs_names.npy')
    for i in range(len(asset_pairs_names_array)):
        try:
            test_data = get_ohlc_data(pair=asset_pairs_names_array[i], interval=1440, since="2024-06-10")
            if test_data is not None:
                print(test_data)
        except Exception as e:
            print(f"Skipping {asset_pairs_names_array[i]} due to error: {e}")