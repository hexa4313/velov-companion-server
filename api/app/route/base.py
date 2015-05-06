import datetime
import logging
from flask import Blueprint, abort
from flask.ext.restful import reqparse
from sqlalchemy import func, and_
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
    token = Token.query.filter(and_(
        and_(Token.user_id == user_id, Token.hash == token),
        Token.expiration_date > current_time)
    ).first()

    if token is None:
        abort(401)

    return user_id
