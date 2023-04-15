# (For educational purposes). A string is entered. It is necessary to replace Cyrillic characters in it with
# the corresponding Latin designations (case-insensitive), and all other characters - with the hyphen character (-).
# To do this, the program defines a dictionary (see the listing). Using it, write a map function that would produce
# the transformed fragments for the input string. Based on this function, form a string consisting of the converted
# fragments (the fragments in the string must follow each other without spaces). Display the result on the screen.

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

print(*list(map(lambda x: t[x] if x in t else '-',
                input("do you have cyrillic keyboard layout? write something: ").lower())), sep='')
