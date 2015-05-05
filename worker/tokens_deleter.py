import os
import sys
import json
import urllib2
import datetime

from model.token import Token
from time import sleep
from sqlalchemy import create_engine
from geoalchemy2.elements import WKTElement
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://' + os.environ['USER'] + ':' +
                       os.environ['PASSWORD'] + '@' +
                       'db/' + os.environ['SCHEMA'])
Session = sessionmaker(bind=engine)


def delete_tokens():

    session = Session()
    current_time = datetime.datetime.utcnow()
    tokens = session.query(Token).filter(
        Token.expiration_date <= current_time).delete()

    session.commit()
    session.close()
