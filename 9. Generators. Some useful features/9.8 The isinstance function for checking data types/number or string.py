# Define a function called get_add that adds either two numbers or two strings (but not a number and a string)
# and returns the result. If the addition cannot be performed, then the function returns None.
# The function signature should be the following:
#
# def get_add(a, b): ...
#
# You don't need to call the function, just define it. Also, nothing needs to be displayed.
#
# P.S. Don't forget about the need to distinguish boolean values ​​(False, True) from integer values.


def get_add(a, b):
    if type(a) == type(b) == str:
        return a + b
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
