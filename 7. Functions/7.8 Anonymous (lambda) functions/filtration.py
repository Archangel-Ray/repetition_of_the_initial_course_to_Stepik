# The program has the function filter_lst (see the program below), which selects the elements
# of the iterable object passed to it and returns the formed tuple of values.
#
# The input of the program is a list of integers written in one line separated by a space.
# Call the filter_lst function to form:
#
# - a tuple of all input list values ​​(passed to the it parameter);
# - a tuple of only negative numbers;
# - a tuple of only non-negative numbers (that is, including 0);
# - a tuple of numbers in the range [3; 5]
#
# Each result of the function should be displayed on a new line with the command:
#
# print(*lst)
#
# where lst is the list per returned by the filter_lst function. To select the desired values, the formal
# key parameter should be passed the appropriate definitions of an anonymous function.


def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


n = list(map(int, input("enter some numeric values: ").split()))
lst = filter_lst(n)
print(*lst)
lst = filter_lst(n, lambda x: x < 0)
print(*lst)
lst = filter_lst(n, lambda x: x >= 0)
print(*lst)
lst = filter_lst(n, lambda x: 3 <= x <= 5)
print(*lst)
