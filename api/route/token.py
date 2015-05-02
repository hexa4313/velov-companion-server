import binascii, os
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import marshal_with
from route.base import api
from flask.ext.bcrypt import check_password_hash

from model.base import db
from model.user import User
from model.token import Token, token_marshaller

class TokenAPI(restful.Resource):

    @marshal_with(token_marshaller)
    def post(self):
        data = request.get_json()

        user = User.query.filter_by(email=data['email']).first()

        if user == None or not check_password_hash(user.password, data['password']):
            abort(401)

        token = Token(user, binascii.hexlify(os.urandom(127)))

        db.session.add(token)
        db.session.commit()

        return token

api.add_resource(TokenAPI, "/token")