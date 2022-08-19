from enum import Enum

from solveme_pytest.src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    """
    Класс для хранения пола пользователя.
    """
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    """
    Класс для хранения статусов пользователя.
    """
    ACTIVE = "active"
    BANNED = "banned"
    DELETED = "deleted"
    INACTIVE = "inactive"
    MERGED = "merged"


class UserErrors(Enum):
    """
    Enum с кастомной ошибкой.
    """
    WRONG_EMAIL = 'Email doesnt contain @'
