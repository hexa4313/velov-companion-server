import datetime
import logging
from flask import Blueprint, abort
from flask.ext.restful import reqparse
from flask.ext import restful
from model.token import Token

blueprint = Blueprint('velov-companion-api', __name__)

api = restful.Api(blueprint, prefix="/api")

def verify_auth():

    parser = reqparse.RequestParser()
    parser.add_argument('Authorization', type=str, location='headers')
    args = parser.parse_args()

    user_id, token = args['Authorization'].split(':')

    current_time = datetime.datetime.utcnow()
    token = Token.query.filter(Token.user_id == user_id and 
    	Token.hash == token and Token.expiration_date > current_time).first()

    if token == None:
        abort(401)

    return user_id