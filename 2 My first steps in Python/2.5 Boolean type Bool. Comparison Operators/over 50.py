# Enter the cost of the book X rubles (for example, X = 435.78) - a positive real number accurate to hundredths (two decimal places). It is required to determine whether the fractional value (the number after the decimal point) is greater than 50. Display True if it is greater and False otherwise. The task is done without using a conditional operator.

price = float(input('Enter the cost of the book: '))
print(price - int(price) > 0.5)
