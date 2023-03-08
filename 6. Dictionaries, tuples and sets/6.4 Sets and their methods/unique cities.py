# The user uses the keyboard to enter city names until they enter the letter q. Determine the total unique number
# of cities entered by the user. Display this number on the screen.
# Of the collections, when implementing the program, use only sets.

cities = set()
city = input('city ​​name: ')
while city != 'q':
    cities.add(city)
    city = input('city ​​name: ')
print(len(cities))
