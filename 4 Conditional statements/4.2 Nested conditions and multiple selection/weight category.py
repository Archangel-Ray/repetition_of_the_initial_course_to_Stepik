# The amateur boxer's weight is entered (in kg, as a real number).
# It is known that the weight is such that a boxer can be assigned
# to one of the weight categories:
#
# 1) light weight - up to 60 kg (inclusive);
# 2) first welterweight - up to 64 kg (inclusive);
# 3) welterweight - up to 69 kg (inclusive);
# 4) the rest - more than 69 kg.
#
# Display the number of the category in which the boxer will compete.

weight = float(input('what is your body weight? '))
if weight <= 60:
    print(1)
elif 60 < weight <= 64:
    print(2)
elif 64 < weight <= 69:
    print(3)
else:
    print(4)
