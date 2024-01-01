import schedule
import time
import timeranges


def printer():
    [print(i) for i in timeranges.time_ranges()]


printer()
schedule.every(0.10).minutes.do(printer)
while True:
    schedule.run_pending()
    time.sleep(0.01)
