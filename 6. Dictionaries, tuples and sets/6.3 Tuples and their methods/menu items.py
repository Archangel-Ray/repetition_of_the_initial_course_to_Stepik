# Menu items are entered (each item on a new line) in the format:
#
# name_1 URL_1
# name_2 URL_2
# ...
# name_N URL_N
#
# It is necessary to present this information as a nested menu tuple in the format:
#
# ((name_1, url_1), (name_2, url_2), ... (name_N, url_N))
#
# Display the result on the screen as a tuple with the command:
#
# print(menu)

lst_in = ['main home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
menu = tuple(tuple(x.split()) for x in lst_in)
print(menu)
