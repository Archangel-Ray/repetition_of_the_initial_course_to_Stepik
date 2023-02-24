# The word is entered. Assign the string 'palindrome' to the msg variable if the entered word is a palindrome
# (it reads the same forward and backward), otherwise, assign the string 'not a palindrome'.
# The check should be done without regard to case. Implement the program using a ternary conditional operator.
# Display the value of the msg variable on the screen.

word = input('enter a word: ').lower()
msg = "palindrome" if word == word[::-1] else "not a palindrome"
print(msg)
