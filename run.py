from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class User (restful.Resource):
    def get(self):
        return {'Cisse': 'Modou'}

api.add_resource(User, '/')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
