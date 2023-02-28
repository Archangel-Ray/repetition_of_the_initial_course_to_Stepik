# A natural number n is entered. Use a for loop to find all divisors of this number.
# The found divisors should be displayed immediately in a column without forming a list.

n = int(input('enter a number: '))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
