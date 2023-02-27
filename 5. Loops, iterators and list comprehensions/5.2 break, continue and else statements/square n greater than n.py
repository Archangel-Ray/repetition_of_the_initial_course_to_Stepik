# A natural number n is entered. Output the first natural number found (that is, iterate over numbers starting from 1)
# whose square is greater than n. Implement the program using a while loop.

n = int(input('enter natural number: '))
count = 1
while True:
    if count**2 > n:
        print(count)
        break
    count += 1
