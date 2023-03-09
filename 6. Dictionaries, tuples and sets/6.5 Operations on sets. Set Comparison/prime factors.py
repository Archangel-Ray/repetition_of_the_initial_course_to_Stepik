# A natural number is entered, which can be determined by the prime factors 1, 2, 3, 5 and 7.
# Do you need to decompose the entered number into the indicated prime factors and check if it
# contains the factors 2, 3 and 5 (all the indicated factors)? If so, print YES, otherwise NO.

n = int(input('enter a multi-digit number: '))
a = set()
b = {1, 2, 3, 5, 7}
for x in b:
    if n % x == 0:
        a.add(x)
print('YES' if {2, 3, 5} < a else 'NO')
