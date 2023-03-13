# Declare a function that takes a string (as an argument) and returns two values ​​as a tuple:
# the given string and its length.
#
# After the function declaration, read (using the input function) a list of city names written on a single line
# separated by a space. Then, using the dictionary generator and the generated function, generate the dictionary d
# in the format:
#
# d = { city 1 : number of characters , ..., city N : number of characters }
#
# Print this dictionary in ascending order of string lengths using the commands:
#
# a = sorted(d, key=lambda x: d[x])
# print(*a)
#
# P.S. For now, just write down these commands. How they work will become clear later, when we take a closer look at
# the sort functions and how the * operator works.


def find_length(line):
    return line, len(line)


list_of_cities = input('write some city names: ').split()
d = {find_length(city_name)[0]: find_length(city_name)[1] for city_name in list_of_cities}
a = sorted(d, key=lambda x: d[x])
print(*a)
