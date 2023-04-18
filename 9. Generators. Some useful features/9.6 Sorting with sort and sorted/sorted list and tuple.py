# The input is a list of integers written in one line separated by a space. Convert this string first to a list
# of integers, and then the list to a tuple of integers. That is, the program will have two different collections:
# a list and a tuple. Sort these collections in ascending order using the sort method,
# if possible, otherwise use the sorted function.
#
# You do not need to display anything on the screen, just form two sorted collections: lst (list) - the result
# of sorting the list; tp_lst (tuple) - the result of sorting the tuple.
#
# P.S. Variables named lst and tp_lst must refer to the results of sorting!

s = input()

lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(sorted(map(int, s.split())))
