import pandas as pd
import schedule
import time
import get_historic_price

today_date = pd.Timestamp.now().date()
current_datetime = pd.Timestamp.now().strftime("%H:%M:%S")

date = "2023-09-19"
hours = "20:00:00"
periods = "14400"
btc_his_price = get_historic_price.get_historic_price(pair='btcusdt', exchange='binance',
                                                      after=date, periods=periods)
high_price = btc_his_price.loc[f"{date} {hours}"]["HighPrice"]
low_price = btc_his_price.loc[f"{date} {hours}"]["LowPrice"]
open_price = btc_his_price.loc[f"{date} {hours}"]["OpenPrice"]
close_price = btc_his_price.loc[f"{date} {hours}"]["ClosePrice"]


def candle_382(high, low, open, close, percentage=0.382):
    # green candle
    gc_frl = high - ((high - low) * percentage)
    # red candle
    rc_frl = high + ((high - low) * percentage)
    if open > close:
        if open > gc_frl:
            return f"Buying pressure at the {int(periods)//3600}-hour candle on {date} at {hours}."
    elif open < close:
        if open < rc_frl:
            return f"Selling pressure at the {int(periods)//3600}-hour candle on {date} at {hours}."
    # no pattern
    return "No 38.2% Candlestick Pattern"


def printer():
    print(candle_382(high=high_price, low=low_price, open=open_price, close=close_price))


printer()
schedule.every(240).minutes.do(printer)
while True:
    schedule.run_pending()
    time.sleep(7200)