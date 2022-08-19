from sqlalchemy import Column, Integer, String, DateTime

from solveme_pytest.db import Model


class Flights(Model):

    """
    Класс описывающий таблицы в базе данных demo.
    """

    __tablename__ = 'flights'

    """
    __tablename__
    Значение должно точно соответствовать названию таблицы в базе данных.
    """

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


class Seats(Model):

    __tablename__ = 'seats'

    aircraft_code = Column(String, primary_key=True)
    seat_no = Column(String, primary_key=True)
    fare_conditions = Column(String)
