# 1 min to 7 days
periods = [60, 180, 300, 900, 1800, 3600, 7200, 14400, 21600, 43200, 86400, 259200, 604800]


def candle_382(high, low, open, close, date, percentage=0.382):
    # green candle
    gc_frl = high - ((high - low) * percentage)
    # red candle
    rc_frl = high + ((high - low) * percentage)
    if open > close:
        if open > gc_frl:
            return f"Buying pressure at the {int(14400) // 3600}-hour candle on {date}."
    elif open < close:
        if open < rc_frl:
            return f"Selling pressure at the {int(14400) // 3600}-hour candle on {date}."
    # no pattern
    return "No 38.2% Candlestick Pattern"


