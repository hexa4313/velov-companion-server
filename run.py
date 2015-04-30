import os
from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@' + os.environ['DB_PORT_5432_TCP_ADDR'] + '/velov-companion'
db = SQLAlchemy(app)
db.create_all()

api = restful.Api(app)

class User (restful.Resource):
    def get(self):
        return {'Cisse': 'Modou'}

api.add_resource(User, '/')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
