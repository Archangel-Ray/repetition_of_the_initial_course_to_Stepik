# Enter two natural even numbers n and m in one line separated by a space, and n m. Print all odd numbers from
# the interval [n, m]. Solve the problem without using the conditional operator. Output the result to the screen
# as a string of numbers separated by a space. Implement the program with a while loop.

n, m = list(map(int, input('enter two natural even numbers: ').split()))
while n < m:
    print(n+1, end=' ')
    n += 2
