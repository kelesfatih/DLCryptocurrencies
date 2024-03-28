import requests
import pandas as pd
import schedule
import time

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


def candle_382(hp, lp, op, cp, date, percentage=0.382):
    hp, lp, op, cp = float(hp), float(lp), float(op), float(cp)
    # green candle
    gc_frl = hp - ((hp - lp) * percentage)
    # red candle
    rc_frl = hp + ((hp - lp) * percentage)
    if op > cp:
        if op > gc_frl:
            return f"Buying pressure on {date}."
    elif op < cp:
        if op < rc_frl:
            return f"Selling pressure on {date}."
    # no pattern
    return f"No 38.2% Candlstick Pattern on {date}."


def time_ranges():
    today_date = pd.Timestamp.now().date()
    date_range = pd.date_range(end=today_date, periods=3, freq="4H")
    btc_his_price = get_historic_price(pair='XBTUSD', interval=240, since="2024-03-14")
    results = []
    for i in date_range:
        high_price = btc_his_price.loc[i]["HighPrice"]
        low_price = btc_his_price.loc[i]["LowPrice"]
        open_price = btc_his_price.loc[i]["OpenPrice"]
        close_price = btc_his_price.loc[i]["ClosePrice"]
        c382 = candle_382(hp=high_price, lp=low_price, op=open_price, cp=close_price, date=i)
        results.append(c382)
    return results


def printer():
    [print(i) for i in time_ranges()]


printer()
schedule.every(1).minutes.do(printer)
while True:
    schedule.run_pending()
    time.sleep(0.01)
