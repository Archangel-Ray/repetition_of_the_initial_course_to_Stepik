# A list of integers is entered into a string separated by a space. Using list comprehension, form a two-dimensional
# list lst of size N x N (a square table of numbers) from them. It is guaranteed that a square matrix (table)
# can be formed from the set of entered numbers. Display the result as a list with the command:
#
# print(lst)

num_line = list(map(int, input('number of numbers must be squared (count: 4, 9, 16, 25...): ').split()))
n = int(len(num_line)**0.5)
lst = [[num_line[i+j] for i in range(n)] for j in range(0, n*n, n)]
print(lst)
