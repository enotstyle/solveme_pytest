from solveme_pytest.db import Session
from solveme_pytest import tables

"""
Пример работы с базой данных без использования фикстуры для 
открытия/закрытия сессии.
"""


session = Session()

result = session.query(
    tables.Flights.flight_id, tables.Flights.status
).filter(
    tables.Flights.flight_id > 10,
    tables.Flights.flight_id < 20
).all()

if result:
    print('all good')
else:
    print('not good')

print(result)

flight_ids = session.query(
    tables.Flights.flight_id
).filter(tables.Flights.flight_id < 30).subquery()

print(flight_ids)
