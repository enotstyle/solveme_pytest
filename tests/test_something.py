import requests

from jsonschema import validate

from ..configuration import SERVICE_URL

from ..src.enums.global_enums import GlobalErrorMessages
# from ..src.schemas.post import POST_SCHEMA
from ..src.baseclasses.response import Response
from ..src.pydantic_schemas.post import Post

def test_equal():
    assert 1 == 1, 'Number is not equal to expected'

def test_is_not_equal():
    assert 1 != 2, 'Number is equal'


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.asser_status_code(200).validate(Post) #или POST_SCHEMA


# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
