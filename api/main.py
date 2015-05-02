import os
from flask import Flask
from model.base import db
from route.base import blueprint

# Register models and routes
import model
import route

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + os.environ['USER'] + ':' +\
                                         os.environ['PASSWORD'] + '@' +\
                                        'db/' + os.environ['SCHEMA']

db.init_app(app)

with app.test_request_context():
    db.create_all()
    db.session.commit()

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)