import ohlc_data
import pandas as pd
from ta.volume import on_balance_volume


def obv_indicator(data_frame, fillna=False):
    data_frame["ClosePrice"] = pd.to_numeric(data_frame["ClosePrice"])
    data_frame["Volume"] = pd.to_numeric(data_frame["Volume"])
    return on_balance_volume(data_frame["ClosePrice"], data_frame["Volume"], fillna=fillna)


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(obv_indicator(price_data))
