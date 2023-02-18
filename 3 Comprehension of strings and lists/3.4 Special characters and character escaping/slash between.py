#Enter two words on one line separated by a space.
# Put a backslash character between these words (instead
# of a space). Display the resulting string on the screen.
#
# P.S. Implement the task without using F-strings.

txt = input('enter some words: ').split()
print(*txt, sep='\\')
