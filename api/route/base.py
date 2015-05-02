from flask import Blueprint
from flask.ext import restful

blueprint = Blueprint('velov-companion-api', __name__)

api = restful.Api(blueprint, prefix="/api")