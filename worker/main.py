import os
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from stations_fetcher import load_stations
from tokens_deleter import delete_tokens

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    load_stations()
    delete_tokens()

    scheduler = BlockingScheduler()
    scheduler.add_job(load_stations, 'interval', seconds=60)
    scheduler.add_job(delete_tokens, 'interval', days=1)
    logging.info('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
