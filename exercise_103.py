# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'
name = "James"
last_name = "Hovell"
species = "human"
eye_colour = "hazel"
hair_colour = "brown"
# Prompt user for input and Re-assign these
# name = input('what new name would you like?')
name = input("Give me your name: ").title()
last_name = input("Give me your last name: ").title()
species = input("Give me your species: ").lower()
eye_colour = input("What colour are your eyes? ").lower()
hair_colour = input("What colour is your hair? ").lower()

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

print(f"Hello {name} {last_name}, you are a {species}, and you have {eye_colour} eyes and {hair_colour} hair!")