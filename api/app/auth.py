import datetime
from model.token import Token


def verify_token(auth):

    user_id, hash = auth.split(':')

    current_time = datetime.datetime.utcnow()
    token = Token.query.filter(Token.user_id == user_id and
                               Token.hash == hash and
                               Token.expiration_date > current_time).first()

    return token is not None
