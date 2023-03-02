# A string is entered. You need to create an iterator to iterate through the characters of this string.
# Then, iterate through the created iterator all the characters up to the first space. In the process of enumeration,
# display characters on the screen in one line one after another (without spaces).
# It is guaranteed that the input string contains at least one space.

string = iter(input('write a proposal: '))
for w in string:
    if w != ' ':
        print(w, end='')
    else:
        break
