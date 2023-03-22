# Two lines of words are entered (words are written with a space). Declare a function that converts these two strings
# into two lists of words and returns those lists.
#
# Define a decorator for this function that forms a dictionary from two lists, where the keys are the words from
# the first list and the values ​​are the corresponding elements from the second list. The resulting dictionary
# should be returned when the decorator is called.
#
# Apply a decorator to the first function and call it on the entered strings.
# Display the result (dictionary d) on the screen with the command:
#
# print(*sorted(d.items()))


def make_dictionary(func):
    def wrapper(lst1, lst2):
        titles, definitions = func(lst1, lst2)
        return dict(zip(titles, definitions))
    return wrapper


@make_dictionary
def get_lists(text_1, text_2):
    text_1 = text_1.split()
    text_2 = text_2.split()
    return text_1, text_2


str1 = input("write multiple values: ")
str2 = input("write as many definitions: ")
d = get_lists(str1, str2)
print(*sorted(d.items()))
