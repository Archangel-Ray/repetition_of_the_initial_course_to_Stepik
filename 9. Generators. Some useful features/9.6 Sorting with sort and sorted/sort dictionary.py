# The input of the function named get_sort is a dictionary, for example, this one:
#
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
#
# It is necessary to sort the dictionary d in descending order of keys (lexicographic sorting of strings)
# and return a list of the corresponding dictionary key values. For example, for the specified dictionary d,
# the result should be a list:
#
# ['дерево', 'лошадь', 'собака', 'кот', 'книга']
#
# The get_sort function signature should be:
#
# def get_sort(d): ...
#
# In the program, you only define a function, you don’t need to call it, and you don’t need to display anything
# on the screen either.
#
# P.S. Hint: the list in the get_sort function is best generated using a list generator.


def get_sort(d):
    return [d[x] for x in sorted(d, reverse=True)]
