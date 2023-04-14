# A natural number N is entered. It is necessary to define a generator function with the name get_sum, which would
# return the current sum of numbers of a sequence of length N in the range of integers [1; N]. For example:
#
# - for the first number 1 sum equal to 1;
# - for the second number 2 a sum equal to 1+2 = 3
# ....
# - for the Nth number a sum equal to 1+2+...+(N-1)+N
#
# Implement the get_sum generator function without using collections.

N = int(input("enter a number: "))


def get_sum(num):
    list_of_numbers = []
    for x in range(1, num + 1):
        list_of_numbers.append(x)
        yield sum(list_of_numbers)


a = get_sum(N)
for s in a:
    print(s, end=" ")
