# coding=utf-8

import os
import sys
import json
import urllib2
import datetime

from model import Token
from time import sleep
from sqlalchemy import create_engine
from geoalchemy2.elements import WKTElement
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://' + os.environ['USER'] + ':' +
                                         os.environ['PASSWORD'] + '@' +
                                         'db/' + os.environ['SCHEMA'])
Session = sessionmaker(bind=engine)

#API_URL à modifier
API_URL = "https://api.jcdecaux.com/vls/v1/stations?contract=Lyon&apiKey={apiKey}"

def delete_tokens():

    apiKey = os.environ['APIKEY']
    if not apiKey:
        sys.exit("No API KEY defined. Did you create conf.env?")

    try:
        r = urllib2.urlopen(API_URL.format(apiKey=apiKey))
        data = json.loads(r.read())
    except (urllib2.URLError, urllib2.HTTPError):
        print "Could not load tokens JSON data."
        return

    if not len(data) > 0:
        print "0 tokens loaded, maybe the data is corrupted?"
        return

    session = Session()
    tokens = session.query(Token)
    for token in tokens:
	if token.expiration_date <= date.today()
	    session.query(token).delete()

    session.commit()
    session.close()

  print "%s token loaded!" % len(data)
