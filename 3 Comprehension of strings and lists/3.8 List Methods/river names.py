# Names of rivers are entered in one line separated by a space.
# You need to sort them all by name (in ascending order) and delete
# the first element in the sorted list. The result is displayed on
# the screen in one line separated by a space.

lst = input('what rivers do you know? ').split()
lst.sort()
lst.pop(0)
print(*lst)
