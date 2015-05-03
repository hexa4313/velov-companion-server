import os

from apscheduler.schedulers.blocking import BlockingScheduler
from stations_fetcher import load_stations
from tokens_deleter import delete_tokens


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(load_stations, 'interval', seconds=60)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    scheduler_24 = BlockingScheduler()
    scheduler_24.add_job(delete_tokens, 'interval', days=1)

    try:
        scheduler.start()
	scheduler_24.start()
    except (KeyboardInterrupt, SystemExit):
        pass
