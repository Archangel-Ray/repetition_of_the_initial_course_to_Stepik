# Using function closures, declare an inner function that wraps the string s in an h1 tag (s is a string,
# a parameter to the inner function). Next, the input of the program receives a string and it must be placed
# in the h1 tag using the implemented closure. Display the result on the screen.
#
# P.S. An example of adding an h1 tag to the string 'Python': h1 Python /h1


def enclose_tag(tag):
    def term_in_the_tag(s):
        return f'<{tag}>{s}</{tag}>'
    return term_in_the_tag


heading = enclose_tag('h1')
print(heading(input("string: ")))
