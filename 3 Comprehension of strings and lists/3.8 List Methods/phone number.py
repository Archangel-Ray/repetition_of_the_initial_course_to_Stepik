# Enter a string with a phone number in the format:
#
# +7(xxx)xxx-xx-xx
#
# It is necessary to convert it to the lst list (character by character,
# that is, the elements of the list will be individual characters of the string).
# Then, remove the first '+', replace the number 7 with 8 and remove the hyphens.
# Display the resulting list on the screen with the command:
#
# print(''.join(lst))

lst = list(input('enter phone number: '))
lst.remove('+')
lst.remove('7')
lst.insert(0, '8')
lst.remove('-')
lst.remove('-')
print("".join(lst))
