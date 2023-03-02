# A list of URLs is entered (each on a new line). It is required to replace all spaces in them with
# a hyphen character (-). Note that there may be several consecutive spaces.
# Display the result of the conversion as strings from URLs.
#
# P.S. To read the entire list, the program has already written the initial lines.

lst_in = ['python.org  about   gettingstarted',
          'python.org  success-stories    category education',
          'stackoverflow.co  company        leadership'
]

for i, string in enumerate(lst_in):
    while string.count('  '):
        string = string.replace('  ', ' ')
    lst_in[i] = string

for i, string in enumerate(lst_in):
    string = string.replace(' ', '-')
    lst_in[i] = string

print(*lst_in, sep='\n')
