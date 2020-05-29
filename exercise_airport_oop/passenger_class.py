# Passenger class
# inherits from people
from exercise_airport_oop.people_class import *
# attributes:
# passport number

class Passenger(People):
    def __init__(self, name, passport_n):
        super().__init__(name)
        self.passport_n = passport_n
