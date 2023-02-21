# Integer numbers are entered in one line separated by a space (at least four).
# You need to find the three smallest numbers in this sequence of numbers and
# display them in ascending order.
# Execute the program without using a conditional statement.

lst = list(map(int, input('enter more than four numbers: ').split()))
min_1 = lst.pop(lst.index(min(lst)))
min_2 = lst.pop(lst.index(min(lst)))
min_3 = lst.pop(lst.index(min(lst)))
print(min_1, min_2, min_3)
