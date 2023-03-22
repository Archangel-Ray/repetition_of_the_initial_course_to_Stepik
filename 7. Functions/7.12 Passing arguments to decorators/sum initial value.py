# A string of integers separated by a space is entered. Write a function that converts this string to a list
# of numbers and returns their sum.
#
# Define a decorator for this function that has one start parameter, the initial sum value.
# Apply a decorator with value start=5 to the function and call the decorated function on the input string s:
#
# s = input()
#
# Display the result on the screen.


def decorator_argument(dec_arg):
    def add_start(incoming_function):
        def wrapper(args):
            return dec_arg + incoming_function(args)
        return wrapper
    return add_start


@decorator_argument(5)
def calculates_sum(list_numbers):
    return sum(list(map(int, list_numbers.split())))


s = input("write some numbers: ")
print(calculates_sum(s))
