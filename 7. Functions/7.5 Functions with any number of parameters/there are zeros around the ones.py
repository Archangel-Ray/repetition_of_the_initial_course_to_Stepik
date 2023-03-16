# A table of integers is entered (see the example below) with size N x N elements (N is determined by the input data).
# This table contains zeros, but in some places - ones. Using a function named verify, which takes a two-dimensional
# list of numbers as input, it is necessary to check whether the ones are isolated from each other, that is,
# there must be zeros around each one.
#
# The following algorithm is recommended. In the verify function, iterate over a two-dimensional list. For each element
# (list) with value 1, call another helper function is_isolate to check if the unit is isolated. That is,
# the is_isolate function must return True if the unit is isolated and False otherwise.
#
# As soon as a non-isolated one is encountered, the verify function must return False. If we successfully reach
# (by elements of the list) to the end, then True is returned.
#
# The function does not need to be executed, only defined.
#
# P.S. When implementing the is_isolate function, you should not write eight if statements. Think about how it can be
# made more beautiful (in terms of the implementation of the algorithm).


def verify(*args):
    for line in range(len(*args) - 1):
        for column in range(len(*args) - 1):
            if args[0][line][column] == 1:
                if args[0][line][column + 1]+args[0][line + 1][column]+args[0][line + 1][column + 1] != 0:
                    return False
    return True


print(verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]))
print(verify([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]))
