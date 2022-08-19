import pytest

from solveme_pytest.src.baseclasses.response import Response
from solveme_pytest.src.schemas.user import User
from solveme_pytest.src.schemas.computer import Computer

from solveme_pytest.examples import computer


def test_getting_users_list(get_users, make_number):
    """
    Тест использующий фикстыру, отдающая и печатающая рандомный номер в тесте
    (make_number), и фикстура (get_users), которая передает объект респонаса в тест.
    Далее объект обрабатывается с помощью Response class и проводим валидацию.
    """
    Response(get_users).asser_status_code(200).validate(User)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23444] Issue is network connection')
def test_another():
    """
    Простой тест, с маркерами и скипом с определенным сообщением.
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    Тест с параметризацией и фикстурой с функциями сложения чисел.
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.development
@pytest.mark.production
def test_another_failing():
    """
    Тест с маркировкой и ожидаемым провалом.
    """
    assert 1 == 2


def test_pydantic_object():
    """
    Парсинг объекта computer по pydemic схеме Computer и получение
    вложенного параметра.
    """
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color)
