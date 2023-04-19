# It is known that the ranks of military personnel have the following order:
#
# private, sergeant, foreman, ensign, lieutenant, captain, major, lieutenant colonel, colonel
#
# The input is a list of military personnel in the format:
#
# name_1=rank_1
# ...
# name_N=rank_N
#
# It is necessary to present the input data in the form of a nested list of the form:
#
# [['name_1', 'rank_1'], ['name_2', 'rank_2'], ..., ['name_N', 'rank_N']]
#
# This list is assigned to a variable named lst. Then, sort it in ascending order.
# You do not need to display anything on the screen, just create a list and point the lst variable to it.

lst_in = ["Athos=lieutenant",
          "Porthos=ensign",
          "d'Artagnan=captain",
          "Aramis=lieutenant",
          "Balakirev=private"
          ]

pattern = dict(zip(['private',
              'sergeant',
              'foreman',
              'ensign',
              'lieutenant',
              'captain',
              'major',
              'lieutenant colonel',
              'colonel'
                    ], range(9)))
lst = list(sorted(map(lambda x: x.split('='), lst_in), key=lambda x: pattern[x[1]]))
print(lst)
