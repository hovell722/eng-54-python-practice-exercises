


# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'


age =''

while age != 'exit':
    age = input("How old are you? ")
    if age == 'exit':
        print('Goodbye!')
        break
    driver_license = input("Can you drive? ")
    if driver_license == 'exit':
        print('Goodbye!')
        break
    age = int(age)
    if driver_license == 'y' and age >= 18:
        print("Now you are and adult!")
    elif driver_license == 'y' and age < 17:
        print("You're not old enough to drive! Don't lie to me!")
    elif driver_license == 'y' and 17 <= age < 18:
        print("Good job on getting your license! You are almost able to vote.")
    elif driver_license == 'n' and age >= 18:
        print("Now you just need to learn to drive!")
    elif driver_license == 'n' and age < 17:
        print("Come back when you are a bit older.")
    elif driver_license == 'n' and 17 <= age < 18:
        print("Now is the perfect time to learn drive, before you can vote!")


