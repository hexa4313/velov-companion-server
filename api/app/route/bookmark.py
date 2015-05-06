from flask.ext.sqlalchemy import get_debug_queries
from flask import request
from werkzeug.exceptions import NotFound
from flask.ext import restful
from flask.ext.restful import marshal_with
from route.base import api
from flask.ext.bcrypt import generate_password_hash
from sqlalchemy import func
from geoalchemy2.elements import WKTElement

from model.base import db
from route.base import verify_auth
from model.user import User
from model.station import Station, station_marshaller


class BookmarkAPI(restful.Resource):

    @marshal_with(station_marshaller)
    def delete(self, station_number):
        user_id = verify_auth()

        station = Station.query.filter_by(number=station_number).first()
        if station is None:
            raise NotFound()

        user = User.query.filter_by(id=user_id).first()
        if user is None:
            raise NotFound()

        user.bookmarks.remove(station)

        db.session.commit()

        return user.bookmarks

    @marshal_with(station_marshaller)
    def put(self, station_number):
        user_id = verify_auth()

        station = Station.query.filter_by(number=station_number).first()
        if station is None:
            raise NotFound()

        user = User.query.filter_by(id=user_id).first()
        if user is None:
            raise NotFound()

        user.bookmarks.append(station)

        db.session.commit()

        return user.bookmarks


class BookmarkListAPI(restful.Resource):

    @marshal_with(station_marshaller)
    def get(self):
        user_id = verify_auth()
        stations = Station.query.filter(Station.users.any(id=user_id)).all()

        return stations

api.add_resource(BookmarkListAPI, "/station/bookmark")
api.add_resource(BookmarkAPI, '/station/bookmark/<station_number>')
