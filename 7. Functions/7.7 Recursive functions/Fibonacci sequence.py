# A natural number N is introduced. Using the recursive function fib_rec(N, f=[]) (here N is the total number of
# Fibonacci numbers; f is the initial list of these numbers), it is necessary to form a sequence
# of Fibonacci numbers according to the rule: the first two numbers are 1 and 1, and each next value is equal
# to the sum of the previous two. An example of such a sequence for the first 7 numbers: 1, 1, 2, 3, 5, 8, 13, ...
#
# The function must return a list of the formed sequence of length N.

N = int(input("enter a number: "))


def fib_rec(N, f=[]):
    if N == 0:
        return 0
    fib_rec(N-1)
    if len(f) < 2:
        f.append(1)
        return f
    else:
        f.append(f[-1]+f[-2])
        return f


print(fib_rec(N))
