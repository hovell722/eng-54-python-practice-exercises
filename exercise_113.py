# functions
# practice using, defining and calling functions

import math

# Build a basic object functional
# phase 1: build function containing add, subtract, multiply, divide.

#  calculate the area of a circle
#  calculate the area of a square
#  calculate the area of a triangle (just find the easiest way)
#  calculate the fiboancci sequence
####

def add(arg1, arg2):
    return arg1 + arg2

def subtract(arg1, arg2):
    return arg1 - arg2

def multiply(arg1, arg2):
    return arg1 * arg2

def divide(arg1, arg2):
    return arg1 / arg2

def circle(r):
    return (r ** 2) * math.pi

def square(width, height):
    return height * width

def triangle(width, height):
    return height * width / 2

def fibonacci(number):
    a = 0
    b = 1
    if number < 0:
        return "Not a valid number"
    elif number == 0:
        return a
    elif number == 1:
        return b
    else:
        for n in range(2, number + 1):
            c = a + b
            a = b
            b = c
        return b


# As a user I want to have a add_funtion()
# that takes in two arguments and add them.
print("calling the add() with 290 and 10, expect 300 to be the result ")
print(add(290, 10) == 300)
print('got:', add(290, 10))

print("calling the subtract() with 290 and 10, expect 280 to be the result ")
print(subtract(290, 10) == 280)
print('got:', subtract(290, 10))

print("calling the multiply() with 20 and 10, expect 200 to be the result ")
print(multiply(20, 10) == 200)
print('got:', multiply(20, 10))

print("calling the divide() with 20 and 10, expect 2 to be the result ")
print(divide(20, 10) == 2)
print('got:', divide(20, 10))

print("calling the circle() with 10, expect 314.1592653589793 to be the result ")
print(circle(10) == 314.1592653589793)
print('got:', circle(10))

print("calling the square() with 10 and 5, expect 50 to be the result ")
print(square(10, 5) == 50)
print('got:', square(10, 5))

print("calling the triangle() with 10 and 5, expect 25 to be the result ")
print(triangle(10, 5) == 25)
print('got:', triangle(10, 5))

print(fibonacci(3))