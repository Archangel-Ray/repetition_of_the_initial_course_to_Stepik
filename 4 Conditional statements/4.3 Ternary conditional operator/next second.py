# Enter the current time (seconds) in the range [0; 59]. If the value is 59, then the next one should be 0.
# And so on in a circle. You need to calculate the next value, checking for a limit value of 59.
# Implement this with a ternary conditional operator. Display the result on the screen.

sec = int(input('enter a number from 0 to 59: '))
print(sec+1 if sec < 59 else 0)
