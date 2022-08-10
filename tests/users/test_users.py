import pytest
import requests

from solveme_pytest.configuration import SERVICE_URL
from solveme_pytest.src.baseclasses.response import Response
from solveme_pytest.src.schemas.user import User

from solveme_pytest.src.schemas.computer import Computer
from solveme_pytest.examples import computer

def test_getting_users_list(get_users, make_number):
    Response(get_users).asser_status_code(200).validate(User)
    # print(make_number)

@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23444] Issue is network connection')
def test_another():
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
    In test we are testing calculating with different values(valid and invalid)
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.development
@pytest.mark.production
def test_another_failing_t():
    """
    In that test we try to check that 1 is equal to 2
    """
    assert 1 == 2

def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color)