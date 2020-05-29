# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'
story = {
    'start' : 'Baby Shoes',
    'middle' : 'For Sale',
    'end' : 'Never Worn'
}
#2 - Print the entire dictionary
print(story)

#3 - Print the type of your dictionary
print(type(story))

#4 - Print only the keys
print(story.keys())

#4 - print only the values
print(story.values())

#5 - print the individual values using the keys (individually, lots of printi commands)
print(story['start'])
print(story['middle'])
print(story['end'])

#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero
story['Author'] = 'Ernest Hemingway'
story['Soundtrack'] = 'Idles'
print(story)