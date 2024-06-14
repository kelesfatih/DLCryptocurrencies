import ohlc_data
import pandas as pd
from ta.volume import force_index


def force_index_13(data_frame, window=13, fillna=False):
    data_frame["ClosePrice"] = pd.to_numeric(data_frame["ClosePrice"])
    data_frame["Volume"] = pd.to_numeric(data_frame["Volume"])
    return force_index(data_frame["ClosePrice"], data_frame["Volume"],
                       window=window, fillna=fillna)


if __name__ == "__main__":
    price_data = ohlc_data.get_ohlc_data(pair="1INCH/EUR", interval=1440, since="2024-02-15")
    print(force_index_13(price_data))
