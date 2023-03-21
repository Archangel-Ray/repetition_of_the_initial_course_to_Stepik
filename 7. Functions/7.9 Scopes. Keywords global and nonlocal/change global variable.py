# There is a program (see listing below) that reads the global variable WIDTH (from the input stream) and a function
# named func1. Add a command in the body of the function that would allow you to change the global variable WIDTH.

WIDTH = int(input("number: "))


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())
