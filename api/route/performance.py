from flask.ext.sqlalchemy import get_debug_queries
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import marshal_with
from route.base import api
from flask.ext.bcrypt import generate_password_hash
from sqlalchemy import func
from geoalchemy2.elements import WKTElement

from model.base import db
from route.base import verify_auth
from model.user import User
from model.performance import Performance, performance_marshaller


class PerformanceAPI(restful.Resource):

    @marshal_with(performance_marshaller)
    def delete(self, performance_number):
        user_id = verify_auth()

        performance = Performance.query.filter_by(
            id=performance_number).first()
        if performance is None:
            abort(404)

        db.session.remove(performance)
        db.session.commit()

        return performance


class PerformanceListAPI(restful.Resource):

    @marshal_with(performance_marshaller)
    def get(self):
        user_id = verify_auth()
        performances = Performance.query.filter(
            Performance.users.any(id=user_id)).all()

        return performances

    @marshal_with(performance_marshaller)
    def post(self):
        user_id = verify_auth()
        data = request.get_json()

        performance = Performance(user_id, data['departure_loc'],
                                  data['arrival_loc'], data['departure_time'],
                                  data['arrival_time'], data['distance'],
                                  data['mean_speed'])

        db.session.add(performance)
        db.session.commit()

        return performance

api.add_resource(PerformanceListAPI, "/performance/")
api.add_resource(PerformanceAPI, '/performance/<performance_number>')
