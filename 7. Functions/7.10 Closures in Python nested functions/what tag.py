# Using function closures, declare an inner function that wraps the string s (s is a string, the parameter
# of the inner function) in an arbitrary tag contained in the tag variable, the parameter of the outer function.
#
# Further, the input of the program receives two lines: the first with a tag, the second with some content.
# The second line must be placed in the tag from the first line using the implemented closure.
# Display the result on the screen.
#
# P.S. An example of adding an h1 tag to the string 'Python': h1 Python /h1


def enclose_tag(tag):
    def term_in_the_tag(s):
        return f'<{tag}>{s}</{tag}>'
    return term_in_the_tag


new_title = enclose_tag(input("tag: "))
print(new_title(input("string: ")))
