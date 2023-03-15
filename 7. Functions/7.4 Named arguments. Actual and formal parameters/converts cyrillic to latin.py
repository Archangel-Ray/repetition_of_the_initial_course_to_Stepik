# Declare a function that takes a Cyrillic string and converts it to Latin using the following dictionary to replace
# Russian letters with the corresponding Latin spelling:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# The function must return the converted string. Do substitutions case-insensitively (translate the source string
# to lower case - small letters). The function also defines a formal parameter sep with an initial value in the form
# of the string '-'. It will define a character to replace spaces in a string.
#
# After the function is declared, read (using the input function) the line and call the function twice
# (with the output of its work on the screen):
#
# - first time with string only
# - second time with string and named argument sep with value '+'.


def convert_cyrillic_to_latin(text, sep='-'):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
         'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
         'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
         'э': 'e', 'ю': 'yu', 'я': 'ya'}
    new_text = ''
    for x in text.lower():
        if x in t:
            new_text += t[x]
        elif x == ' ':
            new_text += sep
        else:
            new_text += x
    return new_text


incoming_text = input("can you write the text in cyrillic? ")
print(convert_cyrillic_to_latin(incoming_text))
print(convert_cyrillic_to_latin(incoming_text, sep='+'))
