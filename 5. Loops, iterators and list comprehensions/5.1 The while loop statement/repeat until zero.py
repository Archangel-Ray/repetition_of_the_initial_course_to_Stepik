# At each iteration of the loop, the user enters an integer. The loop continues until the number 0 is encountered.
# It is necessary to calculate the sum of the numbers entered in the loop and display the result on the screen.
# Implement the program with a while loop.

amount = 0
count = 1
while count != 0:
    count = int(input('enter an integer: '))
    amount += count
print(amount)
