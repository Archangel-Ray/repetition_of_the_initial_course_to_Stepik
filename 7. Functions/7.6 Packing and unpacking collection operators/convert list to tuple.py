# The names of cities are entered in one line separated by a space. Based on this line, you need to form a list of
# names. And then, using the unpacking operator *, convert this list into an lst_c tuple.
# Display the result on the screen with the command:
#
# print(lst_c)

lst = input("write some city names: ").split()
lst_c = (*lst,)
print(lst_c)
