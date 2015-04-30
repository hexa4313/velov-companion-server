from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _lastname = db.Column(db.String(80))
    _firstname = db.Column(db.String(80))
    _email = db.Column(db.String(120), unique=True)
    _birthday = db.column(db.String)

    def __init__(self, lastname, firstname, email, birthday):
        self._lastname = lastname
	self._firstname = firstname
        self._email = email
	self._birthday = birthday

#    def __repr__(self):
#        return '<User %r>' % self.username

