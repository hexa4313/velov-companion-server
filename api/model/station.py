from model.base import db
from geoalchemy2.types import Geography
from flask.ext.restful import fields
from geoalchemy2.shape import to_shape

position_marshaller = {
    'latitude': fields.String(attribute=lambda x: to_shape(x).y),
    'longitude': fields.String(attribute=lambda x: to_shape(x).x)
}

station_marshaller = {
    'number': fields.Integer,
    'name': fields.String,
    'address': fields.String,
    'position': fields.Nested(position_marshaller),
    'banking': fields.Boolean,
    'bonus': fields.Boolean,
    'status': fields.String,
    'bike_stands': fields.Integer,
    'available_bike_stands': fields.Integer,
    'available_bikes': fields.Integer,
    'last_update': fields.DateTime(dt_format='iso8601')
}


class Station(db.Model):
    number = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(127))
    address = db.Column(db.String(255))
    position = db.Column(Geography(geometry_type='POINT', srid=4326))
    banking = db.Column(db.Boolean)
    bonus = db.Column(db.Boolean)
    status = db.Column(db.String(10))
    bike_stands = db.Column(db.Integer)
    available_bike_stands = db.Column(db.Integer)
    available_bikes = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)

    def __init__(self, number, name, address, position, banking, bonus, status,
                 bike_stands, available_bike_stands, available_bikes,
                 last_update):
        self.number = number
        self.name = name
        self.address = address
        self.position = position
        self.banking = banking
        self.bonus = bonus
        self.status = status
        self.bike_stands = bike_stands
        self.available_bike_stands = available_bike_stands
        self.available_bikes = available_bikes
        self.last_update = last_update
