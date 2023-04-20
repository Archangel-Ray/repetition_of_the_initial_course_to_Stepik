# The student grades are entered in one line separated by a space. It is necessary to determine whether there
# is at least one rating below three in this list. If so, then display the line 'expelled', otherwise - 'studies'.
#
# Implement the task using one of the functions: any or all.

print("expelled" if any(map(lambda s: s < 3, map(int, input("grades on a five-point system: ").split())))
      else "studies")
