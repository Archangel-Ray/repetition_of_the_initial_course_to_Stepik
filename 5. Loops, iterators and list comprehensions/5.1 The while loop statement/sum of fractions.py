# A positive integer n is entered. Calculate and display the sum: 1 + 1/2 + 1/3 + ... + 1/n
# up to thousandths (three decimal places). Implement the program with a while loop.

n = int(input('how many times to repeat? '))
count = 1
amount = 0
while count < n+1:
    amount += 1/count
    count += 1
print(round(amount, 3))
