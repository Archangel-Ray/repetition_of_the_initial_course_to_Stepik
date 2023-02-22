# There is a nested list of three lines:
#
# t = [['Tell', 'me', 'uncle', 'after', 'all', 'not', 'for', 'nothing'],
#     ['I', 'Python', 'learned', 'with', 'channel'],
#     ['Balakirev', 'what', 'handed', 'out?']]
#
# It is necessary to implement a check for the presence of the entered word in this list.
# The result (True or False) is displayed on the screen.
# It is necessary to solve the problem without using a conditional operator.

t = [['Tell', 'me', 'uncle', 'after', 'all', 'not', 'for', 'nothing'],
    ['I', 'Python', 'learned', 'with', 'channel'],
    ['Balakirev', 'what', 'handed', 'out?']]

print(input('guess the word in the poem: ') in t[0]+t[1]+t[2])
