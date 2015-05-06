from model.base import db
from geoalchemy2.types import Geography
from flask.ext.restful import fields
from geoalchemy2.shape import to_shape

position_marshaller = {
    'latitude': fields.String(attribute=lambda x: to_shape(x).y),
    'longitude': fields.String(attribute=lambda x: to_shape(x).x)
}

poi_marshaller = {
    'name': fields.String,
    'address': fields.String,
    'position': fields.Nested(position_marshaller)
}


class Poi():
    name = db.Column(db.String(127))
    address = db.Column(db.String(255))
    position = db.Column(Geography(geometry_type='POINT', srid=4326))

    def __init__(self, name, address, position):
        self.name = name
        self.address = address
        self.position = position
