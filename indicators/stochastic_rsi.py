from ta.momentum import StochRSIIndicator
from spot_market_data import ohlc_data


def stochastic_rsi_indicator(data_frame, window=14, smooth1=3, smooth2=3, fillna=False):
    stoch_rsi_object = StochRSIIndicator(data_frame["ClosePrice"], smooth1=smooth1, smooth2=smooth2,
                                         window=window, fillna=fillna)
    return stoch_rsi_object.stochrsi(), stoch_rsi_object.stochrsi_d(), stoch_rsi_object.stochrsi_k()


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)
    print(stochastic_rsi_indicator(price_data))
