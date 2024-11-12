from ta.volatility import (bollinger_hband, bollinger_lband, bollinger_mavg,
                           bollinger_hband_indicator, bollinger_lband_indicator)
from ta.volume import force_index, on_balance_volume
from ta.trend import MACD
from ta.momentum import rsi, StochRSIIndicator


def bollinger_bands(data_frame, window=20, window_dev=2, fillna=False):
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


def force_index_indicator(data_frame, window=13, fillna=False):
    return force_index(data_frame["ClosePrice"], data_frame["Volume"],
                       window=window, fillna=fillna)


def macd_indicator(data_frame, window_fast=12,
                   window_slow=26, window_signal=9,
                   fillna=False):
    macd_object = MACD(data_frame["ClosePrice"], window_fast=window_fast,
                       window_slow=window_slow, window_sign=window_signal,
                       fillna=fillna)
    return macd_object.macd(), macd_object.macd_signal(), macd_object.macd_diff()


def obv_indicator(data_frame, fillna=False):
    return on_balance_volume(data_frame["ClosePrice"], data_frame["Volume"], fillna=fillna)


def rsi_indicator(data_frame, window=14, fillna=False):
    return rsi(data_frame["ClosePrice"], window=window, fillna=fillna)


def stochastic_rsi_indicator(data_frame, window=14, smooth1=3, smooth2=3, fillna=False):
    stoch_rsi_object = StochRSIIndicator(data_frame["ClosePrice"], smooth1=smooth1, smooth2=smooth2,
                                         window=window, fillna=fillna)
    return stoch_rsi_object.stochrsi(), stoch_rsi_object.stochrsi_d(), stoch_rsi_object.stochrsi_k()
