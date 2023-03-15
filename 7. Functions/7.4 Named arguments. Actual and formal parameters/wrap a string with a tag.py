# Declare a function that takes a string and wraps it in the specified tag. The tag is defined by the formal tag
# parameters with the initial value as the string 'h1'. For example, we pass the string 'Hello Python' and wrap
# it in an 'h1' tag. The output should be a string (without quotes):
#
# 'h1 Hello Python /h1'
#
# That is, the h1 tag is opened first, and /h1 is closed at the end of the line. And so for any specified tags.
#
# After the function is declared, read (using the input function) the line and call the function twice
# (with the output of its work on the screen):
#
# - first time with string only
# - second time with string and named argument tag with value 'div'.


def wrap_with_tag(text, tag="h1"):
    return f'<{tag}>{text}</{tag}>'


line_of_text = input("write some text: ")
print(wrap_with_tag(line_of_text))
print(wrap_with_tag(line_of_text, tag='div'))
