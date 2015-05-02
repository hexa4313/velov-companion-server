# coding=utf-8

import os
import sys
import json
import urllib2
import datetime

from model import Station
from time import sleep
from sqlalchemy import create_engine
from geoalchemy2.elements import WKTElement
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://' + os.environ['USER'] + ':' +
                                         os.environ['PASSWORD'] + '@' +
                                         'db/' + os.environ['SCHEMA'])
Session = sessionmaker(bind=engine)

API_URL = "https://api.jcdecaux.com/vls/v1/stations?contract=Lyon&apiKey={apiKey}"

def json_to_station(data):
  lon = data['position']['lng']
  lat = data['position']['lat']
  pos = WKTElement('POINT({0} {1})'.format(lon, lat), srid=4326)
  last_update = datetime.datetime.fromtimestamp(data['last_update'] / 1e3)
  return Station(data['name'], data['address'], pos, data['banking'],
                 data['bonus'], data['status'], data['bike_stands'],
                 data['available_bike_stands'], data['available_bikes'], last_update)

def load_stations():

  apiKey = os.environ['APIKEY']
  if not apiKey:
    sys.exit("No API KEY defined. Did you create conf.env?")

  try:
    r = urllib2.urlopen(API_URL.format(apiKey=apiKey))
    data = json.loads(r.read().replace("°", ""))
  except (urllib2.URLError, urllib2.HTTPError):
    print "Could not load velov stations JSON data."
    return

  if not len(data) > 0:
    print "0 stations loaded, maybe the data is corrupted?"
    return

  session = Session()
  session.query(Station).delete()
  session.add_all(map(json_to_station, data))
  session.commit()
  session.close()

  print "%s stations loaded!" % len(data)