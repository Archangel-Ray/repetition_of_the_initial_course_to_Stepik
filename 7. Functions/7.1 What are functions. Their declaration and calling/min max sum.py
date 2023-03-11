# Declare a function that takes a list, finds the maximum, minimum, and sum of the values ​​of this list,
# and outputs the result as a string (without quotes):
#
# 'Min=v_min, max=v_max, sum=v_sum'
#
# where v_min, v_max, v_sum are the calculated values ​​of the minimum, maximum and sum of the list values.
#
# After declaring the function, read (using the input function) a list of integers written on a single line,
# separated by a space, and call the function with this list.


def compute_statistics(lst):
    print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")


list_of_numbers = list(map(int, input('write some numbers: ').split()))
compute_statistics(list_of_numbers)
