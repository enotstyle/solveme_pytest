from solveme_pytest.src.baseclasses.builder import BuilderBaseClass

from faker import Faker

fake = Faker()

"""
Генератор SeatsBuilder.
"""

class SeatsBuilder(BuilderBaseClass):

    def __init__(self):
        """
        Конструктор очищающий результат и заполняющий его дефолтными значениями.
        """
        super().__init__()
        self.result = {}
        self.reset()

    def set_aircraft_code(self, aircraft_code=fake.word()):
        """
        Сеттер aircraft_code, со значением по умолчанию.
        """
        self.result['aircraft_code'] = aircraft_code
        return self

    def set_seat_no(self, seat_no=fake.word()):
        """
        Сеттер seat_no, со значением по умолчанию.
        """
        self.result['seat_no'] = seat_no
        return self

    def set_fare_conditions(self, fare_conditions=fake.word()):
        """
        Сеттер fare_conditions, со значением по умолчанию.
        """
        self.result['fare_conditions'] = fare_conditions
        return self

    def reset(self):
        """
        Метод для сброса значений на дефолтное.
        """
        self.set_aircraft_code()
        self.set_seat_no()
        self.set_fare_conditions()

    def build(self):
        """
        Возвращает объект.
        """
        return self.result

