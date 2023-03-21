# Declare a function named create_global that has the following signature:
#
# def create_global(x): ...
#
# This function must create a global variable named TOTAL and assign the value x to it. (It should not display
# anything on the screen, only create a variable).
#
# You don't need to call the function, just define it.


def create_global(x):
    global TOTAL
    TOTAL = x

