# Write a program to find all three-digit numbers that, when divided by 47, have a remainder of 43 and
# are a multiple of 3. Print the found numbers in a line separated by a space. Implement the program with a while loop.

n = 100
while n < 1000:
    if n % 47 == 43 and n % 3 == 0:
        print(n, end=' ')
    n += 1
