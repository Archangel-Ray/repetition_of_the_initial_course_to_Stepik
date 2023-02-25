# A natural (that is, a positive integer) number (three-digit or more) is entered. Find the product of all its digits.
# Display the result on the screen. Implement the program with a while loop.

numbers = list(map(int, list(input('enter a more than three-digit number: '))))
count = 0
product = 1
while count < len(numbers):
    product *= numbers[count]
    count += 1
print(product)
