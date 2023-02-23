# A list of cities is entered in one line separated by a space.
# If this list contains the city of Moscow, then delete it.
# Display the resulting list as a string with cities separated by a space.

cities = input('Do you know any cities in Russia? ').split()
if 'Moscow' in cities:
    cities.remove('Moscow')
print(*cities)
