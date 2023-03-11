# Write a function without arguments that reads the first name and last name from the keyboard, written on one line
# separated by a space, and displays a message on the screen (without quotes):
#
# 'Dear, first name! You have correctly completed this task!'
#
# Call this function at the end of the program.


def ask_name():
    name = input('Who are you? ')
    print(f"Dear, {name}! You have correctly completed this task!")


ask_name()
