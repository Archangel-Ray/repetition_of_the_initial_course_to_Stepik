# Two positive integers m and n are entered in one line separated by a space.
# If the number m is evenly divisible by the number n, then display the quotient
# (the result of the division) as an integer. Otherwise,
# display the message 'm is not completely divisible by n' (without quotes)
# and instead of m and n substitute the corresponding numbers,
# for example: '13 is not completely divisible by 2'.

m, n = list(map(int, input('write two positive integers: ').split()))
if m % n == 0:
    print(m//n)
else:
    print(f'{m} is not completely divisible by {n}')
