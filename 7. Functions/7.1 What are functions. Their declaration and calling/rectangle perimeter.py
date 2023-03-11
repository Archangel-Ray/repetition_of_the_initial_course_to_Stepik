# Declare a function with two parameters width and height (width and height of the rectangle)
# that prints a message (without quotes):
#
# 'The perimeter of the rectangle is x'
#
# where x is the calculated perimeter of the rectangle. After the function declaration,
# read (using the input function) two space-separated integers on the same line and call
# the function with these values.


def calculate_perimeter(breadth, level):
    print(f"The perimeter of the rectangle is {(breadth + level) * 2}")


width, height = list(map(int, input('enter two numbers: ').split()))
calculate_perimeter(width, height)
