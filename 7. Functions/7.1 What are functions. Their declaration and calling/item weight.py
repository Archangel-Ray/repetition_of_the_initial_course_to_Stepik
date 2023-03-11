# Declare a function that takes one parameter - the weight of the item and displays
# a message on the screen (without quotes):
#
# 'Item has a weight: x kg.'
#
# where x is the passed function value. After the function declaration, read (using the input function) a real number
# and call the function with that value.


def how_much(weight):
    print(f"Item has a weight: {weight} kg.")


x = float(input('How much does it weigh? '))
how_much(x)
