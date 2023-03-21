# Using function closures, declare an internal function that converts a string from a list of space-separated integers
# to either a list or a tuple. The collection type is determined by the tp parameter of the external function.
# If tp = 'list', then a list is used, otherwise (with a different value) a tuple is used.
#
# Further, two lines are input to the program: the first is the value for the tp parameter; the second is a list
# of integers separated by spaces. Using the implemented closure, transform this data into the appropriate collection.
# Display the result on the screen with the command (lst - link to the collection):
#
# print(lst)


def list_or_tuple(tp):
    def choose_set(list_of_numbers):
        if tp == 'list':
            return list(map(int, list_of_numbers.split()))
        else:
            return tuple(map(int, list_of_numbers.split()))
    return choose_set


repeat_the_conversion = list_or_tuple(input("list or tuple? "))
lst = repeat_the_conversion(input("multiple numbers: "))
print(lst)
