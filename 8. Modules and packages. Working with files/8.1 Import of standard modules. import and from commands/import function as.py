# The program has a factorial function (see listing). At the beginning of the program (before defining a function),
# it is necessary to import a function from the math module with the same name factorial using the from command,
# but in such a way that they do not 'overwrite' each other.
#
# Do not change an already declared function. You don't need to execute functions, just write imports.

from math import factorial as fc


def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p
