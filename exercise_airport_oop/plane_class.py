# define plane class
# it inherits from aircraft
from exercise_airport_oop.aircraft_class import *
# attributes it needs:
    # plane_number

class Plane(Aircraft):
    def __init__(self, cargo, plane_n):
        super().__init__(cargo)
        self.__plane_n = plane_n

