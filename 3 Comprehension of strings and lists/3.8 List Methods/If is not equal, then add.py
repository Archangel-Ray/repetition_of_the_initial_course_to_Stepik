# Enter a string of integers separated by a space. If the first number
# is not equal to the last, then you need to add the True value, otherwise,
# the False value. Display the resulting list lst with the command:
#
# print(*lst)
#
# Implement the task without using conditional statements.

lst = list(map(int, input('enter a string of integers: ').split()))
first_end = lst[0]!=lst[-1]
lst.append(first_end)
print(*lst)
