from flask import request
from flask.ext import restful
from route.base import api

from model.base import db
from model.user import User
import logging


class StationAPI(restful.Resource):
    def post(self):
    	data = request.get_json()
    	station = Station(data['name'], data['address'], data['address2'], data['town'], data['district'], data['lat'], data['lng'], data['bike_stands'], data['banking'])
    	db.session.add(station)
    	db.session.commit()
    	return Station.query.first()

api.add_resource(StationAPI, "/station")
