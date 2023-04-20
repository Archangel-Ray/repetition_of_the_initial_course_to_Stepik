# Declare a function named is_string that takes a collection (list, tuple, set) as input. It should return True if all
# elements of the collection are strings and False otherwise.
#
# The function signature should be the following:
#
# def is_string(lst): ...
#
# You don't need to call the function, just define it. Also, nothing needs to be displayed.
# Implement the task using one of the functions: any or all.


def is_string(lst):
    return all(map(lambda s: isinstance(s, str), lst))
