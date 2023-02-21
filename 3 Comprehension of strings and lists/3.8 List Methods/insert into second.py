# There is a list of cities:
#
# cities = ['Moscow', 'Kazan', 'Yaroslavl']
#
# It is necessary to insert the string 'Ulyanovsk' into the second
# position of this list and display the list with the command:
#
# print(*cities)

cities = ["Moscow", "Kazan", "Yaroslavl"]
cities.insert(1, "Ulyanovsk")
print(*cities)
