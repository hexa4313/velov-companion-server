from model.base import db
from flask.ext.restful import fields

start_performance_marshaller = {
	'departure_loc': fields.String,
	'departure_time': fields.DateTime(dt_format='iso8601'),
	'distance': fields.Float
}

final_performance_marshaller = {
	'departure_loc': fields.String,
	'arrival_loc': fields.String,
	'departure_time': fields.DateTime(dt_format='iso8601'),
	'arrival_time': fields.DateTime(dt_format='iso8601'),
	'distance': fields.Float,
	'mean_speed': fields.Float
}


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    departure_loc = db.Column(db.String(120))
    arrival_loc = db.Column(db.String(120))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    distance = db.Column(db.Float)
    mean_speed = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user, departure_loc, departure_time, distance):
	self.user = user
	self.departure_loc = departure_loc
	self.departure_time = departure_time
	self.distance = distance
