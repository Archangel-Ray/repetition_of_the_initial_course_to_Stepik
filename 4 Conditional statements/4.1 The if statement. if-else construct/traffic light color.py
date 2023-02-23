# The operation of the traffic light for pedestrians is programmed as
# follows: at the beginning of each hour, a green signal is on for three minutes,
# then red for two minutes, green again for three minutes, etc.
# Given a real number t, which means the time in minutes, elapsed since
# the beginning of the next hour. Determine what color signal is on for
# pedestrians at this moment.
# Display the message (without quotes) 'green' for green and 'red' for red.

t = float(input('How many minutes have passed since the beginning of this hour? '))
if t % (3+2) < 3:
    print("green")
else:
    print("red")
