# The word is entered. Check that this word contains all
# three letters: t, h and o (in no particular order).
# Implement the program with a single conditional statement.
# If the test passes, output YES, otherwise NO.

word = input('write a word: ')
if 't' in word and 'h' in word and 'o' in word:
    print('YES')
else:
    print('NO')
