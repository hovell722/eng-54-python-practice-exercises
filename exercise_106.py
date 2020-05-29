# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
# magic_number =
magic_number = 7
# I need to ask user for input
user_number = ''
# I need to check if this input matches a magic_number
while user_number != 'exit':
    user_number = input("Give me a number: ")
    user_number = int(user_number)
    if user_number == magic_number:
        print("Well done! Correct guess!")
        break
    else:
        print("That's the wrong number! Guess again.")

# I need to let the user know if the response was write or not
#self five