import os
import logging
from flask import Flask
from model.base import db
from route.base import blueprint

# Register models and routes
import model
import route

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
# app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' +\
                                        os.environ['USER'] + ':' +\
                                        os.environ['PASSWORD'] + '@' +\
                                        'db/' + os.environ['SCHEMA']

db.init_app(app)

with app.test_request_context():
    db.create_all()
    db.session.commit()

app.register_blueprint(blueprint)
