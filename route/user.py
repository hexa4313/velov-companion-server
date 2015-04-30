import json
from flask import request
from flask.ext import restful
from flask.ext.restful import fields, marshal_with
from route.base import api

from model.base import db
from model.user import User

user_marshaller = {
    'id': fields.String,
    'last_name': fields.String,
    'first_name': fields.String,
    'email': fields.String,
    'birthday': fields.DateTime(dt_format='iso8601')
}

class UserAPI(restful.Resource):

    @marshal_with(user_marshaller)
    def post(self):
    	data = request.get_json()
    	user = User(data['first_name'], data['last_name'], data['email'], data['birthday'])
    	db.session.add(user)
    	db.session.commit()
    	return User.query.filter_by(email=data['email']).first()

api.add_resource(UserAPI, "/user")