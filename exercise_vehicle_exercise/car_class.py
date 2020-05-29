# import my vehicle class
from exercise_vehicle_exercise.vehicle_class import *
# define car class here and make it inherit from vehicle


#Characterists:
# brand
# horse_power
# max_speed

#methods :
# park
# honk

class Car(Vehicle):

    def __init__(self, passengers, cargo, brand, horsepower, speed):
        super().__init__(passengers, cargo)
        self.brand = brand
        self.horsepower = horsepower
        self.speed = speed

    def park(self):
        return 'beep beep beep'

    def honk(self):
        return 'BEEEEPEPEPEPEPEP'