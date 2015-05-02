from model.base import db
from flask.ext.restful import fields

token_marshaller = {
    'user_id': fields.Integer,
    'hash': fields.String
}


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    hash = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user, hash):
        self.user = user
        self.hash = hash