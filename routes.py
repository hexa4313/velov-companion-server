from flask import Blueprint
from flask.ext import restful

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

blueprint = Blueprint('velov-companion-api', __name__)

api = restful.Api(blueprint, prefix="/api")
api.add_resource(HelloWorld, "/helloworld")
