# Two words are entered (separated by a space in one line). The length of the second word is less than the first. From these words, select characters with odd indices, trimming the first word to the length of the second. Compare the received strings with each other for equality and display the result (True or False). Perform the task without using a conditional statement.

word_1, word_2 = input('enter two words: ').split()
print(word_1[:len(word_2)][1::2] == word_2[1::2])
