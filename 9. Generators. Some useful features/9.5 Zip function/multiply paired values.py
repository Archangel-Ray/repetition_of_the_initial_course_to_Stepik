# Two lists of integers are entered. It is necessary to enumerate their elements in pairs and multiply them among
# themselves. When implementing the program, use the zip and map functions. Display the first three values ​​using
# the next function. Values ​​are displayed in a line separated by a space.
# (It is assumed that three output values ​​will always be present).

first_list = map(int, input("enter some numbers: ").split())
second_list = map(int, input("enter some more numbers: ").split())
joint_list = zip(first_list, second_list)
counter = 1
for x in joint_list:
    print(x[0] * x[1], end=' ')
    counter += 1
    if counter > 3:
        break
