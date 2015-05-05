from model.base import db
from flask.ext.restful import fields

user_marshaller = {
    'id': fields.Integer,
    'last_name': fields.String,
    'first_name': fields.String,
    'email': fields.String,
    'birthday': fields.DateTime(dt_format='iso8601')
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

    last_name = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    birthday = db.Column(db.DateTime)

    performances = db.relationship('Performance', backref='user')
    tokens = db.relationship('Token', backref='user')

    bookmarks = db.relationship('Station', secondary=user_bookmarks,
                                backref='users')

    def __init__(self, first_name, last_name, email, password, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birthday = birthday
