# Feat 7. The frog jumps forward and can jump either one space or two at once. Our task is to determine the number
# of route options by which the frog can reach the risk numbered N (a natural number N is entered from the keyboard).
#
#
#
# The problem should be solved using a recursive function. Let's call it get_path. The solution algorithm will be
# the following. Consider, for example, risk number 4. Obviously, a frog can jump into it either from risk number 2
# or from risk number 3. Hence, the total number of options for moving the frog can be determined as:
#
# get_path(4) = get_path(3) + get_path(2)
#
# Similarly, it will be true for any risk N:
#
# get_path(N) = get_path(N-1) + get_path(N-2)
#
# And the initial conditions of the problem are as follows:
#
# get_path(1) = 1
# get_path(2) = 2
#
# Implement a recursive function that should return the number of frog movement options for the line numbered N.
#
# Call this function for the number N entered and display the result on the screen.


N = int(input("how far can a frog jump? enter number: "))


def get_path(N):
    if N in (1, 2):
        return N
    return get_path(N - 1) + get_path(N - 2)


print(get_path(N))
