from model.base import db

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    departure_loc = db.Column(db.String(120))
    arrival_loc = db.Column(db.String(120))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    distance =db.Column(db.Float)
    mean_speed = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user, departure_loc, arrival_loc, departure_time, arrival_time, distance, mean_speed):
        self.user = user
    	self.departure_loc = departure_loc
    	self.arrival_loc = arrival_loc
    	self.departure_time = departure_time
    	self.arrival_time = arrival_time
    	self.distance = distance
    	self.mean_speed = mean_speed