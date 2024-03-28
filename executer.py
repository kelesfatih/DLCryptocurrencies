import schedule
import time
import time_ranges


def printer():
    [print(i) for i in time_ranges.time_ranges()]


printer()
schedule.every(1).minutes.do(printer)
while True:
    schedule.run_pending()
    time.sleep(0.01)
