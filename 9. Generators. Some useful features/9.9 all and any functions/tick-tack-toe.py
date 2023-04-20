# The current playing field for the game 'Tic-tac-toe' is entered in the form of the following table:
#
# # x o
# x # x
# o o #
#
# Here # is a free cell. You need to declare a function named is_free, which receives the playing field as
# a two-dimensional (nested) list as input.
# This function must return True if there is at least one free cell and False otherwise.
#
# The function signature should be the following:
#
# def is_free(lst): ...
#
# You don't need to call the function, just define it. Also, nothing needs to be displayed. Implement the task using
# one of the functions: any or all.
#
# P.S. Reading the input list is not necessary!!! Just define a function.


def is_free(a):
    return any(map(lambda s: '#' in s, a))
