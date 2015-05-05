from sqlalchemy import Column, Integer, String, DateTime
from base import Base


class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)

    hash = Column(String(255))
    expiration_date = Column(DateTime)

    user_id = Column(Integer)
