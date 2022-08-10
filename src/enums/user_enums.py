from enum import Enum

from solveme_pytest.src.baseclasses.pyenum import PyEnum

class Genders(Enum):
    female = 'female'
    male = 'male'

class Statuses(PyEnum):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    BANNED = 'BANNED'

class UserErrors(Enum):
    WRONG_EMAIL = 'Email doesnt contain @'


print(Statuses.list())