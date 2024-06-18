from ta.volume import on_balance_volume
from spot_market_data import ohlc_data


def obv_indicator(data_frame, fillna=False):
    return on_balance_volume(data_frame["ClosePrice"], data_frame["Volume"], fillna=fillna)


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(obv_indicator(price_data))
