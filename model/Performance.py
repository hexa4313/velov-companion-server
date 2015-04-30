from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Performance(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _departure_loc = db.Column(db.String(120))
    _arrival_loc = db.Column(db.String(120))
    _departure_time = db.Column(db.datetime.datetime)
    _arrival_time = db.Column(db.datetime.datetime)
    _distance =db.Column(db.Float)
    _mean_speed = db.Column(db.Float)

    _user_id = db.Column(db.Integer, db.ForeignKey('_user._id')
    _user = db.relationship('User', backref=db.backref('performances', lazy='dynamic'))

    def __init__(self, user, departure_loc, arrival_loc, departure_time, arrival_time, distance, mean_speed):
        self._user = user
	self._departure_loc = departure_loc
	self._arrival_loc = arrival_loc
	self._departure_time = departure_time
	self._arrival_time = arrival_time
	self._distance = distance
	self._mean_speed = mean_speed

#   def __repr__(self):
#        return '<User %r>' % self.username

