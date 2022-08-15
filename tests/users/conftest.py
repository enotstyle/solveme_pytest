import pytest
import requests
from solveme_pytest.configuration import SERVICE_URL

@pytest.fixture()
def get_users():
    response = requests.get(url=SERVICE_URL)
    return response
