# At the entrance of the program, a list of river names is entered, written in one line with a space.
# It is necessary to sort this list in order of decreasing length of names. Report the result in one line with a space.

list_is_named = input("write some river names: ").split()
list_is_named.sort(key=len, reverse=True)
print(*list_is_named)
