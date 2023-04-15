# A table of integers is entered. Using the map function and a list generator, convert the list of strings lst_in
# (see listing) into a two-dimensional list named lst2D containing integers.
#
# You do not need to display anything on the screen, just generate a lst2D list based on the entered data.

lst_in = list(input("enter some numbers: ") for _ in range(4))
lst2D = list(list(map(int, x.split())) for x in lst_in)
print(lst2D)
