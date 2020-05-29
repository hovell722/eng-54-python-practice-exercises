# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []

menu[0] = menu[0].title()
menu[1] = menu[1].title()
menu[2] = menu[2].title()
menu[3] = menu[3].title()
print("Here is the menu")
count = 0
for food in menu:
    count += 1
    print(count, food)
count = 0
while count < 3:
    count += 1
    order = input("What food would you like to order? Give the number: ")
    if order == str(1):
        order = menu[0]
    elif order == str(2):
        order = menu[1]
    elif order == str(3):
        order = menu[2]
    elif order == str(4):
        order = menu[3]
    food_order.append(order)
count = 0
print("You have ordered: ")
for food in food_order:
    count += 1
    print(count, food)



# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything