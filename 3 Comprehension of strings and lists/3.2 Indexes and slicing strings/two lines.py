# Two lines are entered (each on a new line). From the first line, select all characters with even indices, and from the second - with odd ones. Concatenate strings separated by spaces and output to screen.

string_1, string_2 = input('enter the string: '), input('enter the string: ')
print(string_1[::2] +' '+ string_2[1::2])
