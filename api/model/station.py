from model.base import db
from geoalchemy2.types import Geometry


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(127))
    address = db.Column(db.String(255))
    position = db.Column(Geometry(geometry_type='POINT', srid=4326))
    banking = db.Column(db.Boolean)
    bonus = db.Column(db.Boolean)
    status = db.Column(db.String(10))
    bike_stands = db.Column(db.Integer)
    available_bike_stands = db.Column(db.Integer)
    available_bikes = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)

    def __init__(self, name, address, position, banking, bonus, status, bike_stands, available_bike_stands, available_bikes, last_update):
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