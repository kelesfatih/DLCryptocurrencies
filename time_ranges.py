import get_ohlc_data
import candle_382_pattern
import pandas as pd


def time_ranges():
    today_date = pd.Timestamp.now().date()
    date_range = pd.date_range(end=today_date, periods=3, freq="24H")
    btc_his_price = get_ohlc_data.get_historic_price(pair='XBTUSD', interval=1440, since="2024-01-01")
    results = []
    for i in date_range:
        high_price = btc_his_price.loc[i]["HighPrice"]
        low_price = btc_his_price.loc[i]["LowPrice"]
        open_price = btc_his_price.loc[i]["OpenPrice"]
        close_price = btc_his_price.loc[i]["ClosePrice"]
        c382 = candle_382_pattern.candle_382(hp=high_price, lp=low_price, op=open_price, cp=close_price, date=i)
        results.append(c382)
    return results
