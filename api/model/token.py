from model.base import db
from flask.ext.restful import fields
from datetime import timedelta

token_marshaller = {
    'user_id': fields.Integer,
    'hash': fields.String
}


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    hash = db.Column(db.String(255))

    expiration_date = db.Column(db.DateTime)
    duration = timedelta(days=1)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user, hash, expiration_date):
        self.user = user
        self.hash = hash
	self.expiration_date = expiration_date
