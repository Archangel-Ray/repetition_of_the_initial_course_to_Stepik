# I have the following multidimensional list:
#
# d = [1, 2, [True, False], ['Moscow', 'Ufa', [100, 101], ['True', [-2, -1]]], 7.89]
# Using the recursive function get_line_list , create a one-dimensional list based on it from the values ​​
# of the elements of the list d. The function must return the newly created one-dimensional list.
# (Only return, no need to display anything.)
#
# Declare a function with the following signature:
#
# def get_line_list(d,a=[]): ...
# where d is the original list; a - the new one being configured.

d = [1, 2, [True, False], ['Moscow', 'Ufa', [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for i in d:
        if type(i) != list:
            a.append(i)
        else:
            get_line_list(i)
    return a


print(get_line_list(d))
