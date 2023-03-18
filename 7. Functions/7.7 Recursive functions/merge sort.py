# A list of integers is entered in one line separated by a space. You need to sort it in ascending order using
# the merge sort algorithm. The function must return a new sorted list.
# Call the resulting sort function on the given list and display the result on the screen as a sequence
# of space-separated numbers.
#
# Clue. Use recursive functions to split the list and reassemble it.


def merge_sort(first_list, second_list):
    new_list = []
    length_first_list = len(first_list)
    length_second_list = len(second_list)

    index_on_first_list = 0
    index_on_second_list = 0
    while index_on_first_list < length_first_list and index_on_second_list < length_second_list:
        if first_list[index_on_first_list] <= second_list[index_on_second_list]:
            new_list.append(first_list[index_on_first_list])
            index_on_first_list += 1
        else:
            new_list.append(second_list[index_on_second_list])
            index_on_second_list += 1
    new_list += first_list[index_on_first_list:] + second_list[index_on_second_list:]
    return new_list


def division_into_two(a):
    n = len(a) // 2
    b = a[:n]
    c = a[n:]

    if len(b) > 1:
        b = division_into_two(b)
    if len(c) > 1:
        c = division_into_two(c)

    return merge_sort(b, c)


print(*division_into_two(list(map(int, input("write some numbers: ").split()))))
