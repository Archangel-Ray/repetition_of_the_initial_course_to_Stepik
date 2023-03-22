# Declare a function named get_sq that calculates the area of ​​a rectangle given two parameters: the width and height
# of the rectangle. And returns the result (it does not display anything on the screen itself).
# That is, the function has the signature:
#
# def get_sq(width, height): ...
#
# Define a func_show decorator for this function that displays the result on the screen as a string (without quotes):
#
# "Area of ​​rectangle: <value>"
#
# You don't need to call the function and the decorator, just declare it.
# You don't need to apply a decorator to a function either.


def data_output(func):
    def function_start(*args):
        result = func(*args)
        print(f'Area of ​​rectangle: {result}')

    return function_start


def get_sq(width, height):
    return width * height
