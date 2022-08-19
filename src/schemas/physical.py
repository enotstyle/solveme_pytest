from pydantic import BaseModel, HttpUrl, UUID4

from pydantic.color import Color

"""
Пример описания pydantic model с нестандартными типами полей.
"""


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4
