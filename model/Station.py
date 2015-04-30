from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Station(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(80), unique = True)
    _address = db.Column(db.String(120), unique=True)
    _address2 = db.Column(db.String(120))
    _town = db.Column(db.String(80))
    _district = db.Column(db.Integer)
    _bonus = db.Column(db.Boolean)
    _pole = db.Column(db.String(120))
    _lat = db.Column(db.Float)
    _lng = db.Column(db.Float)
    _bike_stands = db.Column(db.Integer)
    _status = db.Column(db.Boolean)
    _available_bike_stands = db.Column(db.Integer)
    _available_bikes = db.Column(db.Integer)
    _availability_code = db.Column(db.Integer)
    _availability = db.Column(db.String(80))
    _banking = db.Column(db.Boolean)
    _gid = db.Column(db.Integer)
    _last_update = db.Column(db.datetime.datetime)
    _last_update_fme = db.Column(db.datetime.datetime)

    def __init__(self, name, address, address2, town, district, lat, lng, bike_stands, banking):
        self._name = name
	self._address = address
	self._address2 = address2
	self._town = town
	self._district = district
	self._lat = lat
	self._lng = lng
	self._bike_stands = bike_Stands
	self._banking = banking

#    def __repr__(self):
#        return '<User %r>' % self.username

