# Declare function with a name get_biggest_city to which can pass any quantity of names of cities through arguments.
# The given function should return the name of city of the greatest length. If it is some such cities, the first found
# (from the greatest). The program to realize without use of sorting.


def get_biggest_city(*args):
    title_length = max([len(name) for name in args])
    for city in args:
        if title_length == len(city):
            return city


print(get_biggest_city(*input("write some city names: ").split()))
