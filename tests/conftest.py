import pytest

from random import randrange

from solveme_pytest.src.generators.player import Player
from solveme_pytest.src.generators.seats_generator import SeatsBuilder

from solveme_pytest import tables

from solveme_pytest.db import Session


@pytest.fixture()
def get_player_generator():
    """
    Фикстура инициализирует объект генератора и передает его в тест.
    """
    return Player()


@pytest.fixture()
def get_seats_generator():
    """
    Фикстура инициализирует объект генератора и передает его в тест.
    """
    return SeatsBuilder


@pytest.fixture
def get_number():
    """
    Метод генерирующий рандомное число.
    """
    return randrange(1, 1000, 5)


def _calculate(a, b):
    """
    Функция с какой-то логикой. При этом фикстура calculate отдает ее в тест как
    объект, чтобы можно было применить в тесте как функцию.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    """
    Фикстура передающая в тест объект _calculate, чтобы в тесте ее можно было
    вызвать как функцию.
    """
    return _calculate


@pytest.fixture
def make_number():
    """
    Фикстура с какой-то логикой, передающая в тест переменную number и после
    прохождения выполняющая часть кода после yield.
    """
    print('im getting number')
    number = randrange(1, 1000, 5)
    yield number
    print(f'Number at home {number}')


@pytest.fixture
def get_db_session():
    """
    Фикстура создающая сессию для работы с базой данных и передающая объект
    сессии в тест и закрывающая сессию после тестов.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_data):
    """
    Функция удаления данных из базы.
    """
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_method(session, item):
    """
    Функция добавления данных в базу.
    """
    session.add(item)
    session.commit()


@pytest.fixture()
def get_add_method():
    """
    Фикстура передающая функцию для добавления тестовых данных в базу как
    объект для дальнейшего использования в тестах.
    """
    return add_method


@pytest.fixture()
def get_delete_method():
    """
    Фикстура передающая функцию для удаления тестовых данных из базы как
    объект для дальнейшего использования в тестах.
    """
    return delete_test_data


@pytest.fixture
def generate_seats(get_db_session, get_seats_generator, get_add_method, get_delete_method):
    """
    Фикстура использующая другие фикстуры, с помощью нее мы можем подготовить
    тестовые данные в базе и передать их в тест, а после удалить из базы.

    В генераторе SeatsBuilder используется библиотека Faker, которая дефолтно вставляет
    невалидные поля, в фикстуре мы вручную передаем ей значения которые примет база.
    """
    item = tables.Seats(**(get_seats_generator().set_aircraft_code('319').set_seat_no('000').set_fare_conditions('Economy').build()))
    get_add_method(get_db_session, item)
    yield item
    get_delete_method(get_db_session, tables.Seats, (tables.Seats.seat_no == item.seat_no))


