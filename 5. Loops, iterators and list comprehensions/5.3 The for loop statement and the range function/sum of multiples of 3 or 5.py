# A natural number n is entered. Calculate the sum of all natural numbers less than n that are multiples
# of either 3 or 5. Display the result (sum). Example: n = 10, we have numbers: 3, 5, 6, 9. Their sum is 23.

s = 0
for i in range(1, int(input('enter a number: '))):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)
