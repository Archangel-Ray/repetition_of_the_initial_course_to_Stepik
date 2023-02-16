# Two words are entered (separated by a space in one line). The length of the first word is less than the second. It is necessary to trim the second word to the length of the first one and display the trimmed word on the screen.

word_1, word_2 = input('enter two words: ').split()
print(word_2[:len(word_1)])
