import pytest
import requests

from solveme_pytest.src.generators.player import Player
from solveme_pytest.src.generators.seats_generator import SeatsBuilder

from solveme_pytest.src.generators.player_localization import PlayerLocalization
from solveme_pytest.src.enums.user_enums import Statuses


from solveme_pytest import tables


@pytest.mark.parametrize('status', Statuses.list())
def test_something1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_something2(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize('localizations', [
    "fr",
    "de",
    "ch",
    'ab'
])
def test_something3(get_player_generator, localizations):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization('fr_FR').set_number(14).build()
    ).build()
    print(object_to_send)


def test_get_data_flights(get_db_session):
    data = get_db_session.query(tables.Flights).first()
    print(data.flight_id)


def test_get_data_seats(get_db_session):
    data = get_db_session.query(tables.Seats.seat_no, tables.Seats.aircraft_code
                                ).filter(tables.Seats.seat_no == '10A').all()
    print(data)


def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.Seats, (tables.Seats.seat_no == '10i'))


def test_try_to_add_testdata(get_db_session, get_add_method, get_seats_generator):
    a = get_seats_generator().set_aircraft_code('319').set_seat_no('020').set_fare_conditions('Economy').build()
    item = tables.Seats(**a)
    get_add_method(get_db_session, item)
    print(item.seat_no, item.fare_conditions, item.aircraft_code)

def test_try_to_add_testdata1(generate_seats):
    print(generate_seats.seat_no, generate_seats.fare_conditions, generate_seats.aircraft_code)


