from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from solveme_pytest.src.enums.user_enums import Statuses
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Network, IPv6Network
from pydantic.color import Color
from solveme_pytest.src.schemas.physical import Physical

from solveme_pytest.examples import computer


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Network
    host_v6: IPv6Network
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)
print(comp)