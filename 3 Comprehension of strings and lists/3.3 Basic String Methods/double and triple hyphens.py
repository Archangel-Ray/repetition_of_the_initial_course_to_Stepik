# A string (slug) is entered. Replace all double dashes (--) and
# triple dashes (---) with single dashes (-) on this line.
# Consider the order in which these substitutions should be made.
# Display the result of the transformation on the screen.

string = input('enter the string: ')
print(string.replace('---', '-').replace('--', '-'))
