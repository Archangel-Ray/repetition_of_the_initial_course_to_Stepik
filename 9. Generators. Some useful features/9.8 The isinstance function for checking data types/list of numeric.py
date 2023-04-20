# Define a function called get_list_dig that returns a list of only the numeric values ​​of the collection
# (list or tuple) passed to it.
#
# The function signature should be the following:
#
# def get_list_dig(lst): ...
#
# You don't need to call the function, just define it. Also, nothing needs to be displayed.
#
# P.S. Don't forget about the need to distinguish boolean values ​​(False, True) from integer values.


def get_list_dig(lst):
    return list(filter(lambda x: type(x) in (int, float), lst))
