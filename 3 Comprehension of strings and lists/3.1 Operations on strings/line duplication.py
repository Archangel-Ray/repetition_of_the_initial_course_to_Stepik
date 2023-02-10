# Write a program to enter two words separated by a space. Form a new string by duplicating the first word twice and the second word three times (all words in the resulting string must be separated by a space). Display the result on the screen.
# The program should be implemented without using F-strings, but using the string duplication operator.

str_1, str_2 = input('enter two words: ').split()
print((str_1 + ' ')*2 + (str_2 + ' ')*3)