from spot_market_data import ohlc_data
import pandas as pd
from ta.volatility import (bollinger_hband, bollinger_lband, bollinger_mavg,
                           bollinger_hband_indicator, bollinger_lband_indicator)


def bollinger_bands(data_frame, window=20, window_dev=2, fillna=False):
    data_frame["ClosePrice"] = pd.to_numeric(data_frame["ClosePrice"])
    return (bollinger_hband(data_frame["ClosePrice"], window=window,
                            window_dev=window_dev, fillna=fillna),
            bollinger_lband(data_frame["ClosePrice"], window=window,
                            window_dev=window_dev, fillna=fillna),
            bollinger_mavg(data_frame["ClosePrice"], window=window,
                           fillna=fillna),
            bollinger_hband_indicator(data_frame["ClosePrice"], window=window,
                                      window_dev=window_dev, fillna=fillna),
            bollinger_lband_indicator(data_frame["ClosePrice"], window=window,
                                      window_dev=window_dev, fillna=fillna))


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(bollinger_bands(price_data))
