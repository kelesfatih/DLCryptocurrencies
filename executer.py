import schedule
import time
import time_ranges


def printer():
    print(time_ranges.time_ranges())


printer()
schedule.every(0.1).minutes.do(printer)
while True:
    schedule.run_pending()
    time.sleep(0.01)
