from sqlalchemy import Column, Integer, String, Boolean, DateTime
from geoalchemy2.types import Geography
from base import Base


class Station(Base):
    __tablename__ = "station"
    number = Column(Integer, primary_key=True)

    name = Column(String(127))
    address = Column(String(255))
    position = Column(Geography(geometry_type='POINT', srid=4326))
    banking = Column(Boolean)
    bonus = Column(Boolean)
    status = Column(String(10))
    bike_stands = Column(Integer)
    available_bike_stands = Column(Integer)
    available_bikes = Column(Integer)
    last_update = Column(DateTime)

    def __init__(self, number, name, address, position, banking, bonus, status, bike_stands, available_bike_stands, available_bikes, last_update):
        self.number = number
        self.name = name
        self.address = address
        self.position = position
        self.banking = banking
        self.bonus = bonus
        self.status = status
        self.bike_stands = bike_stands
        self.available_bike_stands = available_bike_stands
        self.available_bikes = available_bikes
        self.last_update = last_update