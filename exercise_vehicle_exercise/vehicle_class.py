# define vehicle class here

#Characterists:
# n_passangers
# size_cargo

#methods :
# accelerate
# break

class Vehicle():

    def __init__(self, passengers, cargo):
        self.passengers = passengers
        self.cargo = cargo

    def accelerate(self):
        return "Vrooooom"

    def breaking(self):
        return "skkkrrrrrt"
