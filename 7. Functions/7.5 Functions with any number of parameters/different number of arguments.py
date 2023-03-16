# Declare function with a name get_even which accepts any quantity of numbers as arguments
# and returns the list made only from even passed values.


def get_even(*args):
    return [x for x in args if x % 2 == 0]


print(*get_even(*map(int, input("enter some numbers: ").split())))
