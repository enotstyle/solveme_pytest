from pydantic import BaseModel, validator

from solveme_pytest.src.enums.user_enums import Genders, Statuses, UserErrors

"""
Пример описания pydantic model с использованием Enum и validator.
"""


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        """
        Проверяем что в строке содержится знак собаки.
        """
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)

