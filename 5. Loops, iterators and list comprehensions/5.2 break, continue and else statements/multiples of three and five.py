# A natural number n is entered (that is, a positive integer). Loop through all integers in the interval [1; n] and
# form a list of multiples of 3 and 5 at the same time. Output the resulting sequence of numbers as a space-separated
# string if the value of n is less than 100. Otherwise, display the message 'n is too large' (without quotes).
# Use the else statement in the program after the while loop.

n = int(input('enter natural number: '))
count = 1
list_num = []
while count < n+1:
    if n > 99:
        print('n is too large')
        break
    if count % 3 == 0 and count % 5 == 0:
        list_num.append(count)
    count += 1
else:
    print(*list_num)
