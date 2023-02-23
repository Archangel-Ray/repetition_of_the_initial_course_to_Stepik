# The word is entered. It is necessary to determine whether this
# word is a palindrome (it reads the same forward and backward,
# for example, ANNA). Letter case is ignored. If the entered
# word is a palindrome, display YES, otherwise - NO.

word = input('write a word: ').lower()
if word == word[::-1]:
    print('YES')
else:
    print('NO')
