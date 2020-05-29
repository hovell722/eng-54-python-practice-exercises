from exercise_vehicle_exercise.vehicle_class import *
from exercise_vehicle_exercise.car_class import *
from exercise_vehicle_exercise.plane_class import *

vehicle1 = Vehicle(12, 'a lot')
vehicle2 = Vehicle(21, 'a little')

car1 = Car(4, 'small', 'toyota', 20, 50)
car2 = Car(2, 'none', 'ferrari', 200, 300)

plane1 = Plane(200, 'loads', 'emirates', 'long haul')
plane2 = Plane(150, 'nice amount', 'ryanair', 'short haul')

print(vehicle1.passengers)
print(vehicle1.cargo)
print(vehicle1.accelerate())
print(vehicle1.breaking())
