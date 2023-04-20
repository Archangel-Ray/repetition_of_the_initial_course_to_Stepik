# Enter a string of real numbers separated by a space. It is necessary to determine whether there is at least
# one negative among them. Print True if so, False otherwise.
#
# Implement the task using one of the functions: any or all.

print(any(map(lambda s: s < 0, map(float, input("enter some numbers: ").split()))))
