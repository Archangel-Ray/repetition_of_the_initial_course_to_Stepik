# A string is entered with words separated by spaces.
# You need to replace the first space with a single quote,
# and all the rest with double quotes.
# Display the resulting string on the screen.

txt = input('enter a sentence: ')
txt = txt.replace(' ', '\'', 1)
txt = txt.replace(' ', '\"')
print(txt)
