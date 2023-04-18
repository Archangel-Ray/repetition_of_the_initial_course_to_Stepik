# The input of the program is a list of goods in the following format:
#
# name_1:price_1
# ...
# name_N:price_N
#
# It is necessary to convert this list into a dictionary, the keys of which are prices (integers), and the values ​​are
# the corresponding product names. It is necessary to write a function that would take a dictionary as input and return
# a list of the names of the three cheapest goods.
#
# Call this function and display the resulting list on the screen in ascending
# order of price in one line separated by a space.

lst_in = ['smartphone:120000', 'apple:2', 'bag:560', 'pants:2500', 'ruler:10', 'paper:500']
lst_in = dict((int(i[1]), i[0]) for i in (map(lambda x: tuple(x.split(':')), lst_in)))


def for_sorting(dictionary):
    for value in sorted(dictionary):
        yield dictionary[value]


list_values = for_sorting(lst_in)
print(next(list_values), end=' ')
print(next(list_values), end=' ')
print(next(list_values))
