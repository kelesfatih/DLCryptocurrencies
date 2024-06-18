from ta.momentum import rsi
from spot_market_data import ohlc_data


def rsi_indicator(data_frame, window=14, fillna=False):
    return rsi(data_frame["ClosePrice"], window=window, fillna=fillna)


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(type(rsi_indicator(price_data)))
