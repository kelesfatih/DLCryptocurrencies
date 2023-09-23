import requests
import pandas as pd


def get_historic_price(pair, exchange, after, periods):
    url = 'https://api.cryptowat.ch/markets/{exchange}/{pair}/ohlc'.format(
        pair=pair, exchange=exchange)
    resp = requests.get(url, params={
        'periods': periods,
        'after': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data['result'][periods], columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df


if __name__ == "__main__":
    btc = get_historic_price(pair='btcusdt', exchange='binance', after="2023-08-01", periods="14400")
    print(btc)
    print(btc.loc["2023-09-11 00:00:00"])
