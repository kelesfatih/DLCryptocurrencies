def candle_382(high, low, open, close, date, percentage=0.382):
    high, low, open, close = float(high), float(low), float(open), float(close)
    # green candle
    gc_frl = high - ((high - low) * percentage)
    # red candle
    rc_frl = high + ((high - low) * percentage)
    if open > close:
        if open > gc_frl:
            return f"Buying pressure at the {int(1440) // 60} hour candle on {date}."
    elif open < close:
        if open < rc_frl:
            return f"Selling pressure at the {int(1440) // 60} hour candle on {date}."
    # no pattern
    return f"No 38.2% Candlstick Pattern at the {int(1440) // 60} hour candle on {date}."
