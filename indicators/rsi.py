import ohlc_data
import pandas as pd
from ta.momentum import rsi


def rsi_indicator(data_frame, window=14, fillna=False):
    data_frame["ClosePrice"] = pd.to_numeric(data_frame["ClosePrice"])
    return rsi(data_frame["ClosePrice"], window=window, fillna=fillna)


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(rsi_indicator(price_data))
