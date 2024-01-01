import requests
import pandas as pd


def get_historic_price(pair, interval, since):
    url = (f"https://api.kraken.com/0/public/OHLC?pair={pair}".
           format(pair=pair, interval=interval, since=since))
    resp = requests.get(url, params={
        'interval': interval,
        'since': str(int(pd.Timestamp(since).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data["result"]["XXBTZUSD"], columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'VWAP', 'Volume', "Count"
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df


if __name__ == "__main__":
    btc = get_historic_price(pair='XBTUSD', interval=1440, since="2024-01-01")
    print(btc)
