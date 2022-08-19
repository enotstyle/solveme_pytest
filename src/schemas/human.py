from pydantic import BaseModel, validator

"""
Схема Human с валидацией.
"""


class Human(BaseModel):
    name: str
    last_name: str
    surname: str = None
    is_hide: bool

    @validator("is_hide")
    def validate_surname_showing(cls, hide_value, values):
        """
        Пример валидатора, который используется для проверки значения
        в поле is_hide.
        """
        if hide_value is False and values.get('surname') is None:
            raise ValueError("Surname should be presented")
        else:
            return hide_value
