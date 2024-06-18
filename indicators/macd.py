from ta.trend import MACD
from spot_market_data import ohlc_data


def macd_indicator(data_frame, window_fast=12,
                   window_slow=26, window_signal=9,
                   fillna=False):
    macd_object = MACD(data_frame["ClosePrice"], window_fast=window_fast,
                       window_slow=window_slow, window_sign=window_signal,
                       fillna=fillna)
    return macd_object.macd(), macd_object.macd_signal(), macd_object.macd_diff()


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(macd_indicator(price_data))
