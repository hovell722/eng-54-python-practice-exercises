# # Create a little program that ask the user for the following details:
#  - Name
#  - height
#  - favourite color
#  - a secrete number

# Capture these inputs
# Print a tailored welcome message to the user
# print other details gathered, except the secret of course

# hint, think about casting your data type.

name = input("What is you name? ")
name = name.title()
height = int(input("What is your height in cm's? "))
colour = input("What is your favourite colour? ")
number = int(input("Give me a secret number: "))

print(f"Hello {name}, you are {height}cm's tall and your favourite colour is {colour}")