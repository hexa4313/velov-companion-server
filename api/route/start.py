import datetime
from flask.ext.sqlalchemy import get_debug_queries
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import marshal_with, reqparse
from route.base import api
from sqlalchemy import func

from model.base import db
from route.base import verify_auth
from model.station import Station, station_marshaller
from model.user import User
from model.performance import Performance, start_performance_marshaller

class StartAPI(restful.Resource):

    @marshal_with(start_performance_marshaller)
    def post(self):
        user_id = verify_auth()
        user = User.query.filter_by(id=user_id).first()
        if user == None:
            abort(404)

        data = request.get_json()

	departure_station = data['departure_station']
        departure_time = datetime.datetime.utcnow()
	distance = data['distance']

	performance = Performance(user, departure_station, departure_time, distance) 

        return performance

api.add_resource(StartAPI, "/start")
