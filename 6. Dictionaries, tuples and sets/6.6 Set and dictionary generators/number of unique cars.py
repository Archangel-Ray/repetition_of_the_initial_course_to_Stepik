# Cars drove into the car wash throughout the block.
# Their Mrs. the numbers were recorded in the log, as follows (example):
#
# E220SK
# A120MV
# B101AA
# E220SK
# A120MV
#
# On the basis of such a list, use the set generator to generate a list of unique machines.
# Display the number of unique machines on the screen.

lst_in = 'A323GD D456VV B001BB D456VV S111SS'.split()

print(len(set(lst_in)))
