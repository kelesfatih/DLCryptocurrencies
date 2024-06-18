import requests
import numpy as np


# Getting asset pairs from Kraken API
def get_asset_pairs():
    # URL of API
    url = "https://api.kraken.com/0/public/AssetPairs"
    # Requesting data from API
    resp = requests.get(url)
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    data = resp.json()
    return data["result"]


# Getting asset pairs names from Kraken API
def get_asset_pairs_names():
    asset_pairs = get_asset_pairs()
    asset_pairs_names = np.array([i['wsname'] for i in asset_pairs.values() if 'wsname' in i])
    # Save the numpy array to a file
    # np.save('../asset_pairs_names.npy', asset_pairs_names)
    return asset_pairs_names


# Getting USD pairs from Kraken API
def get_usdt_pairs():
    asset_pairs = get_asset_pairs()
    usdt_pairs = np.array([i['wsname'] for i in asset_pairs.values() if 'wsname' in i and 'USDT' in i['wsname']])
    # Save the numpy array to a file
    # np.save('../usdt_pairs.npy', usdt_pairs)
    return usdt_pairs


# Testing the function
if __name__ == "__main__":
    # asset_pairs_names_array = np.load('../asset_pairs_names.npy')
    print(get_usdt_pairs())
