# At each iteration of the loop, an integer is entered. It is necessary to calculate the product of only positive
# numbers, until the value 0 is entered. Implement skipping calculations using the continue statement,
# and also use a while loop. Display the result of the work.

product = 1
n = 1
while True:
    n = int(input('enter the number: '))
    if n < 0:
        continue
    elif n == 0:
        break
    product *= n
print(product)
