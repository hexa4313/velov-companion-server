from model.base import db

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(80), unique = True)
    address = db.Column(db.String(120), unique=True)
    address2 = db.Column(db.String(120))
    town = db.Column(db.String(80))
    district = db.Column(db.Integer)
    bonus = db.Column(db.Boolean)
    pole = db.Column(db.String(120))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    bike_stands = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    available_bike_stands = db.Column(db.Integer)
    available_bikes = db.Column(db.Integer)
    availability_code = db.Column(db.Integer)
    availability = db.Column(db.String(80))
    banking = db.Column(db.Boolean)
    gid = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)
    last_update_fme = db.Column(db.DateTime)

    def __init__(self, name, address, address2, town, district, lat, lng, bike_stands, banking):
        self.name = name
        self.address = address
        self.address2 = address2
        self.town = town
        self.district = district
        self.lat = lat
        self.lng = lng
        self.bike_stands = bike_Stands
        self.banking = banking