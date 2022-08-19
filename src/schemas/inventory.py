from pydantic import BaseModel

"""
Пример простенькой схемы.
"""


class Inventory(BaseModel):
    sold: int
    string: int
    unavailable: int
    pending: int
    available: int
    status: int

