# The text is entered in one line, the words are separated by a space. You need to count the number of unique words
# (case insensitive) in this text. The result (the number of unique words) is displayed on the screen.

print(len(set(input('what proverb do you know? ').lower().split())))
