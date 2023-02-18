# The word is entered. It is necessary to capitalize
# the first letter of this word, and the rest - small.
# Display the result on the screen.

string = input('enter a word: ')
print(string[0].upper()+string[1:].lower())
