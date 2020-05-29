from exercise_vehicle_exercise.vehicle_class import *

class Plane(Vehicle):
    def __init__(self, passengers, cargo, airline, distance):
        super().__init__(passengers, cargo)
        self.airline = airline
        self.distance = distance

    def takeoff(self):
        return 'WOWOWOWOWOOWOW'

    def touchdown(self):
        return 'clap clap clap'