import requests
import pandas as pd


def get_server_time():
    # URL of API
    url = "https://api.kraken.com/0/public/Time"
    # Requesting data from API
    resp = requests.get(url)
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    data = resp.json()
    # Converting timestamp to datetime
    server_time = pd.to_datetime(data["result"]["unixtime"], unit="s")
    return server_time


if __name__ == "__main__":
    print(get_server_time())
