# Declare a function that returns the string passed to it in lower case (with small letters).
# Define a decorator for this function that has one tag parameter that specifies a string with the tag name and
# an initial value of 'h1'. This decorator must wrap the string returned by the function in a tag and return the result.
#
# An example of wrapping the string 'python' in an h1 tag: h1 python /h1
#
# Apply a decorator with value tag='div' to the function and call the decorated function on the input string s:
#
# s = input()
#
# Display the result on the screen.


def decorating_in_tags(tag):
    def incoming_text(func):
        def wrapper(txt):
            return f'<{tag}>{func(txt)}</{tag}>'
        return wrapper
    return incoming_text


@decorating_in_tags('div')
def converts_to_lowercase(more_text):
    return more_text.lower()


s = input("write something: ")
print(converts_to_lowercase(s))
