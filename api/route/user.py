from flask import request, abort
from flask.ext import restful
from flask.ext.restful import marshal_with, reqparse
from route.base import api
from flask.ext.bcrypt import generate_password_hash
from flask.ext.bcrypt import check_password_hash

from model.base import db
from model.user import User, user_marshaller


class UserAPI(restful.Resource):

    @marshal_with(user_marshaller)
    def post(self):
        data = request.get_json()

        hashed_password = generate_password_hash(data['password'])
        user = User(data['first_name'], data['last_name'],
                    data['email'], hashed_password, data['birthday'])
        db.session.add(user)
        db.session.commit()

        return user

    @marshal_with(user_marshaller)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help='email is required')
        parser.add_argument('password', required=True,
                            help='password is required')
        args = parser.parse_args()

        user = User.query.filter_by(email=args['email']).first()
        if user is None or\
           not check_password_hash(user.password, args['password']):
            abort(401)

        return user

api.add_resource(UserAPI, "/user")
