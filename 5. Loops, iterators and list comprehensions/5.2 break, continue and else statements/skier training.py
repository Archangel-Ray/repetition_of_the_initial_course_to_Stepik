# (To use a while loop). Having started training, the skier ran 10 km on the first day. Each next day, he increased
# the run by 10% of the previous day's run. Determine on which day he will run more than x km (a natural number x
# is entered from the keyboard). The result (the desired day) is displayed on the screen.

x = int(input('how far can a skier run? '))
run = 10
count = 1
while run < x:
    run += run/100*10
    count += 1
print(count)
