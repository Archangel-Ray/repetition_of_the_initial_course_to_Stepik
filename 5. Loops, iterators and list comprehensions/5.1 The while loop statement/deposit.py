# On January 1, a citizen opened a bank account by investing $1000. Each year the amount of the deposit increases by 5%
# of the available amount. Determine the amount of the deposit after n years (n is a positive integer entered from
# the keyboard). The result is rounded up to hundredths and displayed on the screen.
# Implement the program with a while loop.

n = int(input('how many years? '))
count = 0
deposit = 1000
while count < n:
    deposit += deposit/100*5
    count += 1
print(round(deposit, 2))
