from flask import request
from flask.ext import restful
from route.base import api

from model.base import db
from model.user import User
import logging


class UserAPI(restful.Resource):
    def post(self):
    	data = request.get_json()
    	user = User(data['first_name'], data['last_name'], data['email'], data['birthday'])
    	db.session.add(user)
    	db.session.commit()
    	return User.query.filter_by(email=data['email']).first()

api.add_resource(UserAPI, "/user")