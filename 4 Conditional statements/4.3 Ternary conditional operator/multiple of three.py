# An integer is entered. It is necessary to assign to the msg variable the string 'a multiple of 3' if the entered
# number is a multiple of 3, otherwise it must be assigned the string 'not a multiple of 3'.
# Implement the program using the ternary operator. Display the msg variable on the screen.

num = int(input('enter the number: '))
msg = "a multiple of 3" if num % 3 == 0 else "not a multiple of 3"
print(msg)
