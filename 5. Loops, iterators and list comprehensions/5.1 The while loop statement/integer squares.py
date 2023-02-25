# Two positive integers n and m are introduced, moreover, n m. Output into a string space-separated
# squares of integers in the range [n; m]. Implement the program with a while loop.

n, m = list(map(int, input('enter two positive integers: ').split()))
while n <= m:
    print(n**2, end=' ')
    n += 1
