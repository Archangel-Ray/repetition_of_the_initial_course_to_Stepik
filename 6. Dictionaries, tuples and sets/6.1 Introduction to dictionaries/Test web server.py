# The test web server returns HTML pages by URLs (strings). The program receives various URLs as input. If the address
# came for the first time, then display the string on the screen (without quotes):
#
# 'HTML-page for address URL'
#
# If the address comes again, then you should take the string 'HTML page for address URL address' from the dictionary
# and display a message on the screen (without quotes):
#
# 'Fetched from cache: HTML-page for address URL'
#
# Display messages each on a new line.

lst_in = ['stepik.org-course-100707-syllabus',
          'stepik.org-course-100707-info',
          'stepik.org-catalog',
          'stepik.org-course-100707-info',
          'stepik.org-course-100707-syllabus',
          'stepik.org-course-124803-promo'
          ]
d = {}
for i in lst_in:
    if i not in d:
        d[i] = 'HTML-page for address ' + i
        print('HTML-page for address', i)
    else:
        print('Fetched from cache:', d[i])
