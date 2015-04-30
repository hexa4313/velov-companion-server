from flask import request
from flask.ext import restful
from flask.ext.restful import marshal_with
from route.base import api

from model.base import db
from model.user import User, user_marshaller

class UserAPI(restful.Resource):

    @marshal_with(user_marshaller)
    def post(self):
        data = request.get_json()

        user = User(data['first_name'], data['last_name'], data['email'], data['birthday'])
        # TODO : PASSWORD ! + HASHING
        db.session.add(user)
        db.session.commit()

        return user

api.add_resource(UserAPI, "/user")