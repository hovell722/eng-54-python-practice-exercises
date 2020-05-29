# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????

lol_mains = ['Quinn', 'Singed', 'Nunu', 'Anivia', 'Karthus']

# Print the lists and check it's type
print(lol_mains)
print(type(lol_mains))
# Print the list's first object
print(lol_mains[0])

# Print the list's second object
print(lol_mains[1])

# Print the list's last object
print(lol_mains[-1])

# Re-define the first item on the list and
lol_mains[0] = 'Malzahar'

# Re-define another item on the list and print all the list
lol_mains[1] = 'Jarvan IV'
print(lol_mains)
# Add an item to the list and print the list
lol_mains.append('Blitzcrank')
print(lol_mains)
# Remove an item from the list and print the list
lol_mains.remove('Nunu')
print(lol_mains)
# Add two items to list and print the list
lol_mains.extend(['Ahri', 'Twitch'])
print(lol_mains)



