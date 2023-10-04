import schedule
import time
import timeranges


def printer():
    print(timeranges.time_ranges())


printer()
schedule.every(0.1).minutes.do(printer)
while True:
    schedule.run_pending()
    time.sleep(0.01)
