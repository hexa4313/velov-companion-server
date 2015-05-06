from flask import request, abort
from flask.ext import restful
from flask.ext.restful import marshal_with, reqparse
from route.base import api
from flask.ext.bcrypt import generate_password_hash
from flask.ext.bcrypt import check_password_hash

from model.base import db
from route.base import verify_auth
from model.user import User, user_marshaller


class UserAPI(restful.Resource):

    @marshal_with(user_marshaller)
    def post(self):
        data = request.get_json()

        hashed_password = generate_password_hash(data['password'])
        user = User(data['email'], hashed_password)
        db.session.add(user)
        db.session.commit()

        return user

    @marshal_with(user_marshaller)
    def get(self):
        user_id = verify_auth()

        user = User.query.filter_by(id=user_id).first()

        return user

api.add_resource(UserAPI, "/user")
