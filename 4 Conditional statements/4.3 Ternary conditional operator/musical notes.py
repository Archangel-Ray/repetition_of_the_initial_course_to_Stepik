# There is a list of base notes:
#
# m = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
#
# Enter three integers in the range from 1 to 7 - the numbers of notes, in one line separated by a space.
# It is necessary to display the specified notes as a string separated by a space,
# but before the notes to and f, additionally put the sharp symbol '#'.
# Implement this program using a ternary conditional operator (it can be used multiple times).

m = ['', 'do', 're', 'mi', 'fa', 'sol', 'la', 'si']
a, b, c = list(map(int, input('enter three numbers between 1 and 7: ').split()))
print('#'+m[a] if a == 1 or a == 4 else m[a], end=' ')
print('#'+m[b] if b == 1 or b == 4 else m[b], end=' ')
print('#'+m[c] if c == 1 or c == 4 else m[c])
