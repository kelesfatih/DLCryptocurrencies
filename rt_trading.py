from spot_market_data import server_time, system_status, ohlc_data, asset_pairs

if system_status.get_system_status() == "online":
    print("System is online")
else:
    print("System is offline")
