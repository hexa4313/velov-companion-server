import binascii, os
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import marshal_with
from route.base import api

from model.base import db
from model.user import User
from model.token import Token, token_marshaller

class TokenAPI(restful.Resource):

    @marshal_with(token_marshaller)
    def post(self):
        data = request.get_json()

        # TODO : verify password here !
        user = User.query.filter_by(email=data['email']).first()

        if user is None:
            abort(401)

        token = Token(user, binascii.hexlify(os.urandom(127)))

        db.session.add(token)
        db.session.commit()

        return token

api.add_resource(TokenAPI, "/token")