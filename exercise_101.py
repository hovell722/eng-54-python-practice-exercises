# Practice strings
# Welcome to Sparta - exercise

# Version 1 specs - with concatenation
# define a variable name, and assign a string
sparta = "stringy"
# prompt the user for input and ask the user for his/her name
# re assign the original variable this this input
sparta = input("Give me your name: ")
# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print("Hello " + sparta.strip() + " how are you today?")
# Version 2 - with interpolation
print(f"Hello {sparta.strip()} how are you today?")
# ask the user for a first name, save it in a variable
first_name = input("Give me your first name: ")
# ask the user for a last name, save it in a variable
last_name = input("Give me your last name: ")
# use interpolation to print the message
print(f"Your name is {first_name.title()} {last_name.title()}")

# Calculate year of birth
# gather details on age and name
age = input(f"How old are you {first_name.title()} {last_name.title()}?")
age = int(age)
print(f"{first_name.title()} {last_name.title()} was born in {2020 - age}")
# print something like
# OMG <person>, you are <age> years old so you were born in <year>