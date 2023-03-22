# Declare a function named get_list with the following description in the body of the function:
#
# '''Function for generating a list of integer values'''
#
# The function itself must form and return a list of integers,
# which comes to its input as a string of integers separated by a space.
#
# Define a decorator that sums the values ​​from the list of this function and returns the result.
# Inside the decorator, decorate the passed get_list function with the @wraps command (don't forget to import:
# from functools import wraps). This decoration is necessary so that the original get_list function preserves
# its local properties: __name__ and __doc__.
#
# Apply a decorator to the get_list function, but don't call it.


from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(args):
        return sum(func(args))
    return wrapper


@decorator
def get_list(multiple_numbers):
    '''Function for generating a list of integer values'''
    return list(map(int, multiple_numbers.split()))
