# A natural number n is entered. It is necessary to form a list using list comprehension, consisting of divisors of the
# number n (including the number n itself). The result is displayed on the screen in one line separated by a space.

n = int(input('numeric: '))
print(*[x for x in range(1, n+2) if n % x == 0])
