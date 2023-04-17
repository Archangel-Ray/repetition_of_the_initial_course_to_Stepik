# Enter a list of items in the form of a list
#
# Using the map function, you must first convert this list of strings into a tuple whose elements are also tuples:
#
# (('name_1', 'weight_1'), ..., ('name_N', 'weight_N'))
#
# And then filter out (exclude) all items with a weight less than 500 using the filter function.
# Display a list of the remaining items (only their names) on one line separated by a space.
#
# P.S. To read the entire list, the program has already written the initial lines.

lst_in = ['umbrella=1000', 'tent=10000', 'matches=22', 'bowler=543']

tuple_of_tuples = tuple(map(lambda x: tuple(x.split('=')), lst_in))
filtered_tuple = filter(lambda x: int(x[1]) > 500, tuple_of_tuples)
for value in filtered_tuple:
    print(value[0], end=' ')
