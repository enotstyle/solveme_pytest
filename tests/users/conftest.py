import pytest
import requests

from solveme_pytest.configuration import SERVICE_URL

@pytest.fixture
def get_users():
    """
    Фикстура передающая в тест ответ от сервера.
    """
    response = requests.get(url=SERVICE_URL)
    return response
