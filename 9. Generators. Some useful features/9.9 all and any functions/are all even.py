# A string of integers separated by a space is entered.
# It is necessary to determine whether all these numbers are even. Print True if so, False otherwise.
#
# Implement the task using one of the functions: any or all.

print(all(map(lambda s: s % 2 == 0, map(int, input("enter some numbers: ").split()))))
