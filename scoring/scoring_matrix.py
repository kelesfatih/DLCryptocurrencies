from indicators import bollinger_bands, force_index, macd, on_balance_volume, rsi, stochastic_rsi
from spot_market_data import ohlc_data, server_time


class ScoringMatrix:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.score = 0

    def rsi_scoring(self):
        if rsi.rsi_indicator(self.data_frame).loc[str(server_time.get_server_time())] < 30:
            self.score += 1
        elif rsi.rsi_indicator(self.data_frame).loc[str(server_time.get_server_time())] > 70:
            self.score -= 1
        return self.score


if __name__ == '__main__':
    print(ScoringMatrix(ohlc_data.get_ohlc_data(pair="BTC/USDT", interval=1440)).rsi_scoring())
