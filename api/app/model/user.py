from model.base import db
from flask.ext.restful import fields

user_marshaller = {
    'id': fields.Integer,
    'email': fields.String
}

user_bookmarks = db.Table('user_bookmarks',
                          db.Column('user_id', db.Integer,
                                    db.ForeignKey('users.id')),
                          db.Column('station_number', db.Integer,
                                    db.ForeignKey('station.number'))
                          )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))

    performances = db.relationship('Performance', backref='user')
    tokens = db.relationship('Token', backref='user')

    bookmarks = db.relationship('Station', secondary=user_bookmarks,
                                backref='users')

    def __init__(self, email, password):
        self.email = email
        self.password = password
