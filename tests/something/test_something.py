import pytest
import requests

from solveme_pytest.src.generators.player_localization import PlayerLocalization
from solveme_pytest.src.enums.user_enums import Statuses
from solveme_pytest.src.schemas.human import Human
from solveme_pytest.src.baseclasses.response import Response
from solveme_pytest.src.schemas.inventory import Inventory

from solveme_pytest.examples import human

from solveme_pytest import tables

"""
В этом файле рассмотрим примеры работы:
 1. С базой данных
 2. Параметризация ключей и поочерёдное их удаление
 3. Использование генератора в тестах 
 4. Кастомная генерацию локализаций
"""


@pytest.mark.parametrize('status', Statuses.list())
def test_generator_changing(status, get_player_generator):
    """
    Работаем с генератором, который был получен с помощью фикстуры.
    """
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_deleting_keys_in_object(delete_key, get_player_generator):
    """
    Пример удаляющий поочередно поля с помощью параметризации у объекта,
    который отдала нам фикстура.
    """
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize('localizations', [
    "fr",
    "de",
    "ch",
    'ab'
])
def test_updating_localization_in_generator(get_player_generator, localizations):
    """
    В этом примере получаем генератор get_player_generator и BuilderBaseClass, который находится
    ниже уровнем. Когда получили их, мы меняем локализацию в генераторе исходя из параметров,
    создаем экземпляр и заменяем им наш главный объект.
    """
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization('fr_FR').set_number(14).build()
    ).build()
    print(object_to_send)


def test_inventory():
    """
    В данном примере получаем данные и валидируем их через класс Response, т.к достать
    данные через get('data') не получится - перепресвоил атрибут объекта на r.json().
    """
    r = requests.get('https://petstore.swagger.io/v2/store/inventory')
    response = Response(r)
    response.response_json = r.json()
    response.validate(Inventory)


def test_human():
    """
    Пример отправки запроса, получения данных и использование Response class, для
    работы с валидацией данных.
    """
    r = Human.parse_obj(human)
    print(r.validate_surname_showing(r.is_hide, r))


def test_get_data_flights(get_db_session):
    """
    Получение сессии базы данных из фикстуры get_db_session и используем ее для
    того, чтобы достать данные из таблицы.
    """
    data = get_db_session.query(tables.Flights).first()
    print(data.flight_id)


def test_get_data_seats(get_db_session):
    """
    Получаем сессию, делаем запрос на seat_no и aircraft_code, выводим только
    seat_no == '10A
    """
    data = get_db_session.query(tables.Seats.seat_no, tables.Seats.aircraft_code
                                ).filter(tables.Seats.seat_no == '10A').all()
    print(data)


def test_try_to_delete_something(get_delete_method, get_db_session):
    """
    Пример удаления данных из базы, если мы не знаем ID, с помощью фикстуры.
    """
    # тут какой-то код
    get_delete_method(get_db_session, tables.Seats, (tables.Seats.seat_no == '10i'))


def test_try_to_add_testdata(get_db_session, get_add_method, get_seats_generator):
    """
    Пример добавления в базу данных в самом тесте, без использования фикстуры.
    """
    a = get_seats_generator().set_aircraft_code('319').set_seat_no('026').set_fare_conditions('Economy').build()
    item = tables.Seats(**a)
    get_add_method(get_db_session, item)
    print(item.seat_no, item.fare_conditions, item.aircraft_code)


def test_try_to_add_testdata1(generate_seats):
    """
    Пример создания и удаления данных после работы в базе с помощью фикстуры.
    """
    print(generate_seats.seat_no, generate_seats.fare_conditions, generate_seats.aircraft_code)
