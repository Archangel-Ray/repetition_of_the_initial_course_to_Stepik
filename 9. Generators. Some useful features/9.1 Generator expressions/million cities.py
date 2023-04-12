# There is a list of city names:
#
# cities = ['Moscow', 'Ulyanovsk', 'Samara', 'Ufa', 'Omsk', 'Tula']
#
# It is necessary to write a generator that, using this list, would produce 1,000,000 city names in a cycle.
# That is, having reached the end of the list, it returned to the beginning and repeated the enumeration.
# And so, for the issuance of a million names.
# Display the first 20 city names using a generator in one line separated by a space.

cities = ['Moscow', 'Ulyanovsk', 'Samara', 'Ufa', 'Omsk', 'Tula']
index_generator = (cities[index % len(cities)] for index in range(1000000))
for x in range(20):
    print(next(index_generator), end=' ')
