from model.base import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    last_name = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.String)
    
    performances = db.relationship('Performance', backref='user', lazy='dynamic')

    def __init__(self, first_name, last_name, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday