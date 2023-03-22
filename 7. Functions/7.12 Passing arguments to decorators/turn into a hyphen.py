# Declare a function that takes a Cyrillic string and converts it to Latin using the following dictionary to replace
# Russian letters with the corresponding Latin spelling:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# The function must return the converted string. Do substitutions case-insensitively (translate the source string
# to lower case - small letters).
#
# Define a decorator with a chars parameter and an initial value of '!?' that converts the given characters
# to a '-' character and, in addition, all consecutive hyphens (such as '--' or '---') results in a single hyphen.
# The result should be returned as a string.
#
# Apply a decorator with argument chars='?!:;,.' to the function and call the decorated function on the input string s:
#
# s = input()
#
# Display the result on the screen.


def what_characters(chars=" !?"):
    def incoming_function(func):
        def wrapper(incoming_text):
            incoming_text = func(incoming_text)
            new_text = ''
            for letter in incoming_text:
                if letter in chars:
                    new_text += '-'
                else:
                    new_text += letter
            while '--' in new_text:
                new_text = new_text.replace('--', '-')
            return new_text
        return wrapper
    return incoming_function


@what_characters("?!:;,. ")
def cyrillic_to_latin(incoming_text):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
         'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
         'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
         'э': 'e', 'ю': 'yu', 'я': 'ya'}
    new_text = ''
    for letter in incoming_text.lower():
        if letter in t:
            new_text += t[letter]
        else:
            new_text += letter
    return new_text


s = input("if you can write in Cyrillic, then write something: ")
print(cyrillic_to_latin(s))
