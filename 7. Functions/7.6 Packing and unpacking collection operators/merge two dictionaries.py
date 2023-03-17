# There is a dictionary containing menu items:
#
# menu = {'Home': 'home', 'Archive': 'archive', 'News': 'news'}
#
# Additionally, more menu items are introduced as strings in the format:
#
# title_1=url_1
# ...
# name_N=url_N
#
# It is necessary to convert this entered information into a dictionary and add it to the menu dictionary using
# the unpacking operator for dictionaries. The variable menu should lead to the resulting dictionary.

lst_in = {'Cities': 'about-cities', 'Cars': 'read-of-cars', 'Airplanes': 'airplanes'}
menu = {'Home': 'home', 'Archive': 'archive', 'News': 'news'}
menu = {**menu, **lst_in}
print(menu)
