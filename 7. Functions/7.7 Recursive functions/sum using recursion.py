# Enter a list of integers in one line separated by a space. You need to calculate the sum of these input values
# ​​using a recursive function (to iterate over the elements of a list) called get_rec_sum. The function must return
# the value of the sum. (It should not display anything on the screen).
#
# Call this function and display the calculated sum value on the screen.


lst = list(map(int, input("enter some numbers: ").split()))


def get_rec_sum(n):
    if len(n) == 0:
        return 0
    return n.pop() + get_rec_sum(n)


print(get_rec_sum(lst))
