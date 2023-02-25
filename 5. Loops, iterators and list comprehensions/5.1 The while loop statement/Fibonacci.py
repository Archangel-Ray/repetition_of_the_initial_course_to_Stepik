# The Fibonacci sequence is formed as follows: the first two numbers are 1 and 1, and each subsequent number is equal
# to the sum of the two previous ones. We have the following sequence of numbers: 1, 1, 2, 3, 5, 8, 13, ...
# Construct a Fibonacci sequence of length n (n is entered from the keyboard).
# Display the result as a string of received numbers, separated by a space. Implement the program with a while loop.

a, b = 0, 1
count = 0
n = int(input('how many iterations? '))
while count < n:
    a, b = b, a+b
    print(a, end=' ')
    count += 1
