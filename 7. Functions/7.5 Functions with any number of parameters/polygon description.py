# Declare a function named get_data_fig to calculate the perimeter of an arbitrary N-gon.
# N side lengths are passed to the input of this function via arguments.
# Additionally, named arguments can be specified:
#
# type-boolean value True/False
# color-integer value
# closed-boolean value True/False
# width - integer value
#
# The function should return as a tuple the polygon perimeter and the specified values of named parameters
# in the order they are listed in the task text (if they were passed).
# If a parameter is omitted, you don't need to return it (skip it).


def get_data_fig(*args, **kwargs):
    polygon_perimeter = sum(args)
    answer = [polygon_perimeter]
    if 'type' in kwargs:
        answer.append(kwargs['type'])
    if 'color' in kwargs:
        answer.append(kwargs['color'])
    if 'closed' in kwargs:
        answer.append(kwargs['closed'])
    if 'width' in kwargs:
        answer.append(kwargs['width'])
    return answer


polygon_side_lengths = list(map(int, input("enter several side lengths of the polygon: ").split()))
print(get_data_fig(*polygon_side_lengths, type=True, closed=False, width=5))
