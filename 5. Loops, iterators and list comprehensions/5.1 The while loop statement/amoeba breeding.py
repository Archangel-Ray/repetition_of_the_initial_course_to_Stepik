# A unicellular amoeba divides into 2 cells every 3 hours. Determine how many cells there will be in n hours
# (n is a positive integer entered from the keyboard). Assume that there was originally one amoeba.
# Display the result on the screen. The problem must be solved using a while loop.

n = int(input('how many hours will we breed? '))
count = 0
unicellular = 1
while count < n//3:
    unicellular *= 2
    count += 1
print(unicellular)
