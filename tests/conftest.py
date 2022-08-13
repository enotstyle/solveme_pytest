import pytest
import requests
from random import randrange
from solveme_pytest.src.generators.player import Player
from solveme_pytest.db import Session
from solveme_pytest.src.generators.seats_generator import SeatsBuilder
from solveme_pytest import tables

@pytest.fixture()
def get_player_generator():
    return Player()

@pytest.fixture()
def get_seats_generator():
    return SeatsBuilder

@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    print('im getting number')
    number = randrange(1, 1000, 5)
    yield number
    print(f'Number at home {number}')


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()

def add_method(session, item):
    session.add(item)
    session.commit()

@pytest.fixture()
def get_add_method():
    return add_method

@pytest.fixture()
def get_delete_method():
    return delete_test_data


@pytest.fixture
def generate_seats(get_db_session, get_seats_generator, get_add_method, get_delete_method):
    item = tables.Seats(**(get_seats_generator().set_aircraft_code('319').set_seat_no('023').set_fare_conditions('Economy').build()))
    get_add_method(get_db_session, item)
    yield item
    get_delete_method(get_db_session, tables.Seats, (tables.Seats.seat_no == item.seat_no))
