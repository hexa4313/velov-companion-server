import os

from apscheduler.schedulers.blocking import BlockingScheduler
from stations_fetcher import load_stations


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(load_stations, 'interval', seconds=60)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
