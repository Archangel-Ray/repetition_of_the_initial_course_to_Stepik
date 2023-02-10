# A real number is entered. You need to check that it falls into either the range [0; 2] or in the range [10; 20] (inclusive). Display True if it hits and False otherwise. The task is done without using a conditional operator.

x = float(input('Enter a real number: '))
print(0 <= x <= 2 or 10 <= x <= 20)
