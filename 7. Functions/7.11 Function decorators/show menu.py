# The input of the program receives a string with the names of menu items, written in one line separated by a space.
# You need to define a function called get_menu that converts this string into a list of words and returns that list.
# The function signature is as follows:
#
# def get_menu(s): ...
#
# Define a decorator for this function called show_menu that displays the list on the screen in the format:
# 1. Item_1
# 2. Item_1
# ...
# N. Item_N
#
# Apply the show_menu decorator to the get_menu function using the @ operator.
# Nothing more needs to be done in the program. Do not call the functions themselves.


def show_menu(func):
    def wrapper(a):
        result = func(a)
        for item in range(1, len(result)+1):
            print(f'{item}. {result[item-1]}')
    return wrapper


@show_menu
def get_menu(s):
    return s.split()
