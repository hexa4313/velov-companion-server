import os
import traceback
import sys
import json
import urllib2
import datetime
import logging

from model.station import Station
from time import sleep
from sqlalchemy import create_engine
from geoalchemy2.elements import WKTElement
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://' + os.environ['USER'] + ':' +
                       os.environ['PASSWORD'] + '@' +
                       'db/' + os.environ['SCHEMA'])
Session = sessionmaker(bind=engine)

API_URL = "https://api.jcdecaux.com/vls/v1/stations" +\
          "?contract=Lyon&apiKey={apiKey}"


def json_to_station(data):
    lon = data['position']['lng']
    lat = data['position']['lat']
    last_update = data['last_update']
    pos = WKTElement('POINT({0} {1})'.format(lon, lat), srid=4326)

    if last_update:
        last_update = datetime.datetime.fromtimestamp(last_update / 1e3)
    else:
        last_update = datetime.datetime.today()

    return Station(data['number'], data['name'], data['address'], pos,
                   data['banking'], data['bonus'], data['status'],
                   data['bike_stands'], data['available_bike_stands'],
                   data['available_bikes'], last_update)


def load_stations():

    apiKey = os.environ['APIKEY']
    if not apiKey:
        sys.exit("No API KEY defined. Did you create conf.env?")

    url = API_URL.format(apiKey=apiKey)
    try:
        data = json.load(urllib2.urlopen(url=url, timeout=10))
    except (urllib2.URLError, urllib2.HTTPError):
        logging.error(traceback.format_exc())
        logging.error("Could not load velov stations JSON data.")
        logging.error("URL : " + url)
        return

    if not len(data) > 0:
        logging.error("0 stations loaded, maybe the data is corrupted?")
        return

    session = Session()
    session.query(Station).delete()
    session.add_all(map(json_to_station, data))
    session.commit()
    session.close()

    logging.info("{0} stations loaded!".format(len(data)))
