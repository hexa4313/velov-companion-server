from flask.ext.sqlalchemy import get_debug_queries
from flask import request
from flask.ext import restful
from flask.ext.restful import marshal_with, reqparse
from route.base import api
from flask.ext.bcrypt import generate_password_hash
from sqlalchemy import func
from geoalchemy2.elements import WKTElement

from model.base import db
from model.station import Station, station_marshaller


class StationAPI(restful.Resource):

    @marshal_with(station_marshaller)
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('lng', type=float, required=True,
                            help='longitude is required')
        parser.add_argument('lat', type=float, required=True,
                            help='latitude is required')
        parser.add_argument('radius', type=float, required=True,
                            help='radius is required')
        args = parser.parse_args()

        point = WKTElement('POINT({0} {1})'.format(args['lng'], args['lat']),
                           srid=4326)
        stations = db.session.query(Station).filter(
            func.ST_DWithin(Station.position, point, args['radius'])
            ).all()

        return stations

api.add_resource(StationAPI, "/station")
