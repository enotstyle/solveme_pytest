import requests

from solveme_pytest.configuration import SERVICE_URL
from solveme_pytest.src.baseclasses.response import Response
from solveme_pytest.src.schemas.user import User


def test_getting_users_list(get_users, make_number):
    Response(get_users).asser_status_code(200).validate(User)
    print(make_number)


def test_another():
    assert 1 == 1

