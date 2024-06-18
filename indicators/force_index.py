from ta.volume import force_index
from spot_market_data import ohlc_data


def force_index_indicator(data_frame, window=13, fillna=False):
    return force_index(data_frame["ClosePrice"], data_frame["Volume"],
                       window=window, fillna=fillna)


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(force_index_indicator(price_data))
