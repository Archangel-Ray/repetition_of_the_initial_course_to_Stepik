# A real number is entered. It is necessary to determine that its integer part is a multiple of 3. Display True if it is a multiple and False otherwise. The task is done without using a conditional operator.

print(int(float(input('Enter a real number: '))) % 3 == 0)