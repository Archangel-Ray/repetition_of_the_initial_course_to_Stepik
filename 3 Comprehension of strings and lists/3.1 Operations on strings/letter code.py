# Two letters are entered from the keyboard (in one line separated by a space). Display the following
# line on the screen: "Codes: letter1 = letter1 code, letter2 = letter2 code"

letter_1, letter_2 = input('enter two letters: ').split()
print('Codes: ' + letter_1 + ' = ' + str(ord(letter_1)) + ', ' + letter_2 + ' = ' + str(ord(letter_2)))