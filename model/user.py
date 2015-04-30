from model.base import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    lastname = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.String)
    
    performances = db.relationship('Performance', backref='user', lazy='dynamic')

    def __init__(self, lastname, firstname, email, birthday):
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.birthday = birthday