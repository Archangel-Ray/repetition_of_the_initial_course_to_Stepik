# Declare a function that takes a Cyrillic string and converts it to Latin using the following dictionary to replace
# Russian letters with the corresponding Latin spelling:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# The function must return the converted string. Do substitutions case-insensitively (translate the source string
# to lower case - small letters). All non-alphabetic characters ': ;.,_' should be converted to '-' (hyphen).
#
# Define a decorator for this function that turns multiple consecutive hyphens into a single hyphen.
# The resulting string should be returned when the decorator is called.
# (The decorator itself should not display anything on the screen).
#
# Apply a decorator to the first function and call it for the input Cyrillic string s:
#
# s = input()
#
# Display the result of the decorated function on the screen.


def extra_dashes(func):
    def wrapper(text):
        result = func(text)
        while '--' in result:
            result = result.replace('--', '-')
        return result
    return wrapper


@extra_dashes
def cyrillic_conversion(lines):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    encoded_text = ''
    for let in lines.lower():
        if let in t:
            encoded_text += t[let]
        elif let in ': ;.,_':
            encoded_text += '-'
        else:
            encoded_text += let
    return encoded_text


text_line = input("can you write in cyrillic? write something: ")
print(cyrillic_conversion(text_line))
