# The input of the program is a string of integers separated by a space. Write a get_list function that converts
# this string into a list of integers and returns it. Define a decorator for this function that sorts
# the list of numbers in ascending order. The sort result should be returned when the decorator is called.
#
# Call the decorated get_list function and display the resulting sorted list lst with the command:
#
# print(*lst)


def sort_numbers(func):
    def wrapper(arg):
        result = func(arg)
        result.sort()
        return result
    return wrapper


@sort_numbers
def get_list(s):
    return list(map(int, s.split()))


lst = get_list(input("write some numbers: "))
print(*lst)
