#Flight Trip class
from exercise_airport_oop.plane_class import *
# origin
# Destination
# list of passengers
# plane number

# need some getters nd setter:

# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin
# As a user I can add a Passenger to the list of passengers

class Flight:
    def __init__(self, origin, destination, plane_n):
        self.origin = origin
        self.destination = destination
        self.__plane_n = plane_n
        self.passengers_list = []



