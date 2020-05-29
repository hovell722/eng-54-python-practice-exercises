# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

number = ''

while number != 'exit':
    number = input("Give me a number: ")
    if number.isdigit():
        number = int(number)
        for n in range(1, number + 1):
            if (n % 5 == 0) and (n % 3 == 0):
                print("bizzzzuu")
            elif n % 5 == 0:
                print("zzuu")
            elif n % 3 == 0:
                print("bizz")
            else:
                print(n)
    elif number == 'exit':
        print("Goodbye!")
        break
