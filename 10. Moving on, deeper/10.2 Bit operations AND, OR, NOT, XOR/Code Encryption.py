# The encrypted word is entered. Encryption of the character codes of this word was carried out using the bitwise XOR
# operation with key=123. That is, each character was converted according to the algorithm:
#
# x = ord(x) ^ key
#
# Here ord is a function that returns the character code x. Unscramble the entered word and display it on the screen.
#
# P.S. Hint: to convert the code to a character, use the chr function.

print(*[chr(ord(x) ^ 123) for x in input()], sep="")
