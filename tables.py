from sqlalchemy import Boolean, Column, Integer, String, DateTime

from db import Model


class Flights(Model):

    __tablename__ = 'flights'

    flight_id = Column(Integer, primary_key=True)
    flight_no = Column(String)
    scheduled_departure = Column(DateTime(timezone=True))
    scheduled_arrival = Column(DateTime(timezone=True))
    departure_airport = Column(String)
    arrival_airport = Column(String)
    status = Column(String)
    aircraft_code = Column(String)
    actual_departure = Column(DateTime(timezone=True))
    actual_arrival = Column(DateTime(timezone=True))
