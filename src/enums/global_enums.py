from enum import Enum


class GlobalErrorMessages(Enum):
    """
    Класс с ошибками.
    """
    WRONG_STATUS_CODE = 'Expected code is not equal to expected (200)'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal to expected'
