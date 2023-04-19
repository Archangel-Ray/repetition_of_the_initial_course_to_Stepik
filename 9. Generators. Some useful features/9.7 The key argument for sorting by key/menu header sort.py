# There is a table with data presented in the format:
#
# Number;Name;Score;Pass
# 1;Ivanov;3;Yes
# 2;Petrov;2;No
# ...
# N;Balakirev;4;Yes
#
# This data must be represented as a two-dimensional (nested) tuple. All numbers must be represented as whole numbers.
# Then, sort the data so that the columns are in order:
#
# Name;Pass;Score;Number
#
# Implement this operation using sorting. The result should also be represented as a two-dimensional tuple and assigned
# to a variable named t_sorted.
#
# The program should not display anything, only form a two-dimensional tuple with the t_sorted variable.

lst_in = ["Number;Name;Score;Pass",
          "1;Porthos;5;Yes",
          "2;Aramis;3;Yes",
          "3;Athos;4;Yes",
          "4;d'Artagnan;2;No",
          "5;Balakirev;1;No"
          ]
t = tuple(tuple(int(b) if b.isdigit() else b for b in a) for a in map(lambda x: tuple(x.split(';')), lst_in))
t_sorted = tuple((x[1], x[3], x[2], x[0]) for x in t)
