# The list of books in the bookstore is entered in the following format:
#
# author 1 : title 1
# ...
# author N : title N
#
# Authors with titles can be repeated. It is necessary, using generators, to form a dictionary named d of the form:
#
# {'author 1': {'title 1', 'title 2', ..., 'title M'}, ..., 'author K': {'title 1', 'title 2', ... , 'Name S'}}
#
# That is, the keys are unique authors, and the values ​​are sets with unique titles of the books
# of the corresponding author.


lst_in = list()
author = '!'
while author:
    author = input('book author: ').capitalize()
    title = input('book title: ').capitalize()
    if author:
        lst_in.append(f'{author}: {title}')

d = {}
for book in lst_in:
    the_author, the_title = book.split(':')
    if the_author not in d:
        d[the_author] = {the_title.strip()}
    else:
        d[the_author].add(the_title.strip())

print(d)
