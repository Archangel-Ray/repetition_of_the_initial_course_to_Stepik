# Enter two integer values ​​a and b (a b) in one line separated by a space. It is necessary to form a list of integers
# from a to b (inclusive) with a change step of 1, using the range function, the [] operator, and the unpacking
# operator *. Display the resulting list on the screen with the command:
#
# print(*lst)

a, b = map(int, input("Enter two integers, the first is less than the second: ").split())
lst = (*range(a, b+1),)
print(*lst)
