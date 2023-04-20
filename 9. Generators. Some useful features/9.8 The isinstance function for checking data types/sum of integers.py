# Define a function called get_sum that takes an iterable (list, string, tuple, dictionary, set) as input
# and calculates the sum of only the integers taken from the elements of the iterable.
# The calculated amount is returned by the function. If there are no integers, then 0 is returned.
#
# The function signature should be the following:
#
# def get_sum(it): ...
#
# You don't need to call the function, just define it. Also, nothing needs to be displayed.
#
# Function input argument examples:
#
# get_sum([1,2,3, 'a', True, [4, 5], 'c', (4, 5)])
# get_sum({5, 6, 7, '8', 5, '4'})
# get_sum((10, 'f', '33', True, 12))
# get_sum(['1', True, False, (1, 23)])
#
# P.S. Don't forget about the need to distinguish boolean values ​​(False, True) from integer values.


def get_sum(it):
    return sum(filter(lambda x: type(x) is int, it))
