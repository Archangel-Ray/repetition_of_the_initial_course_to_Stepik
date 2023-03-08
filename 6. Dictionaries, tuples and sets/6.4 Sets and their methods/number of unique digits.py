# A string containing Latin characters, spaces and numbers is entered. It is necessary to select from it all
# non-repeating digits (characters from 0 to 9) and display them in one line separated by a space in ascending order
# of values. If there are no digits, then output the word NO.

s = set()
for x in input('What is your favorite holiday and when is it? '):
    if x.isdigit():
        s.add(x)
if len(s) != 0:
    print(*sorted(s))
else:
    print('NO')
