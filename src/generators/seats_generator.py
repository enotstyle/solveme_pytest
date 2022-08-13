from solveme_pytest.src.baseclasses.builder import BuilderBaseClass

from faker import Faker

fake = Faker()

class SeatsBuilder(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_aircraft_code(self, aircraft_code=fake.word()):
        self.result['aircraft_code'] = aircraft_code
        return self

    def set_seat_no(self, seat_no=fake.word()):
        self.result['seat_no'] = seat_no
        return self

    def set_fare_conditions(self, fare_conditions=fake.word()):
        self.result['fare_conditions'] = fare_conditions
        return self

    def reset(self):
        self.set_aircraft_code()
        self.set_seat_no()
        self.set_fare_conditions()

    def build(self):
        return self.result

