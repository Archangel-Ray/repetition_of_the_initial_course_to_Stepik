# Define a function named get_even_sum that takes an iterable (list, string, tuple, dictionary, set) as input
# and calculates the sum of only even integers taken from the elements of the iterable.
# The result is returned by the function. If there are no integers, then 0 is returned.
#
# The function signature should be the following:
#
# def get_even_sum(it): ...
#
# You don't need to call the function, just define it. Also, nothing needs to be displayed.
#
# P.S. Don't forget about the need to distinguish boolean values ​​(False, True) from integer values.


def get_even_sum(it):
    return sum(filter(lambda x: type(x) is int and x % 2 == 0, it))
