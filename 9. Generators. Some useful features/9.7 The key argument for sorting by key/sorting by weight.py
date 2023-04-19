# The input of the program is a string in the format:
#
# item_1=weight_1
# ...
# item_N=weight_N
#
# The weights of the items are given as integers. It is necessary to form a dictionary on the basis of these data and,
# then, on the basis of this dictionary, form a list of items in descending order of their weight.
# (The list should contain only the names of items without their weights).
#
# Display the result as a string with names separated by a space.

lst_in = ['scissors=100', 'bowler=500', 'matches=20', 'lighter=40', 'mirror=50']
lst_in = dict((int(i[1]), i[0]) for i in (map(lambda x: tuple(x.split('=')), lst_in)))
print(*list(lst_in[x] for x in sorted(lst_in, reverse=True)))
