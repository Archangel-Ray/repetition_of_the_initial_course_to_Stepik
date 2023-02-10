# Write a program for entering a string and forming a new string of the form:
# 'String: input string . Length: string length'.
# Display the result of the generated string on the screen.
# P.S. Do not use F-strings in the program.

string = input('enter the string: ')
print('String: ' + string + '. Length: ' + str(len(string)))