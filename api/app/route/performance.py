from flask.ext.sqlalchemy import get_debug_queries
from flask import request
from werkzeug.exceptions import NotFound
from flask.ext import restful
from flask.ext.restful import marshal_with
from route.base import api
from flask.ext.bcrypt import generate_password_hash
from sqlalchemy import func

from model.base import db
from route.base import verify_auth
from model.user import User
from model.performance import Performance
from model.performance import final_performance_marshaller
from model.performance import start_performance_marshaller


class PerformanceAPI(restful.Resource):

    @marshal_with(final_performance_marshaller)
    def delete(self, performance_number):
        user_id = verify_auth()

        performance = Performance.query.filter_by(
            id=performance_number).first()
        if performance is None:
            raise NotFound()

        db.session.remove(performance)
        db.session.commit()

        return performance

    @marshal_with(final_performance_marshaller)
    def put(self, performance_number):
        user_id = verify_auth()
        data = request.get_json()

        performance = Performance.query.filter_by(
            id=performance_number).first()
        if performance is None:
            raise NotFound()

        performance.arrival_loc = data['arrival_loc']
        performance.arrival_time = datetime.datetime.utcnow()

        duration = (performance.arrival_time - performance.departure_time
                    ).total_seconds()
        # mean_speed in m/s --> performance.distance in meter
        mean_speed = performance.distance / duration

        db.session.remove(performance)
        db.session.add(performance)
        db.session.commit()

        return performance


class PerformanceListAPI(restful.Resource):

    @marshal_with(final_performance_marshaller)
    def get(self):
        user_id = verify_auth()
        performances = Performance.query.filter(
            Performance.users.any(id=user_id)).all()

        return performances

    @marshal_with(start_performance_marshaller)
    def post(self):
        user_id = verify_auth()
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            raise NotFound()

        data = request.get_json()

        departure_station = data['departure_station']
        departure_time = datetime.datetime.utcnow()
        distance = data['distance']

        performance = Performance(user, departure_station,
                                  departure_time, distance)

        return performance

api.add_resource(PerformanceListAPI, "/performance/")
api.add_resource(PerformanceAPI, '/performance/<performance_number>')
