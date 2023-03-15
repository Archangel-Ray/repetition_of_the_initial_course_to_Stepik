# Functions from the previous lesson, add another formal parameter up with an initial boolean value of True.
# If the up parameter is True, then the tag (specified in the formal tag parameter) should be written in capital
# letters, otherwise - in small letters.
#
# After the function is declared, read (using the input function) the line and call the function twice
# (with the output of its work on the screen):
#
# - first time with string and named argument tag with value 'div'
# - the second time with a string named argument tag with value 'div' and named argument up with value False.


def wrap_with_tag(text, tag="h1", up=True):
    if up:
        return f'<{tag.upper()}>{text}</{tag.upper()}>'
    else:
        return f'<{tag}>{text}</{tag}>'


line_of_text = input("write some text: ")
print(wrap_with_tag(line_of_text, 'div'))
print(wrap_with_tag(line_of_text, 'div', False))
