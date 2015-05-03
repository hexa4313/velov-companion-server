from model.base import db
from flask.ext.restful import fields

token_marshaller = {
    'hash': fields.String,
    'expiration_date': fields.DateTime(dt_format='iso8601')
}


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    hash = db.Column(db.String(255))
    expiration_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user, hash, expiration_date):
        self.user = user
        self.hash = hash
        self.expiration_date = expiration_date