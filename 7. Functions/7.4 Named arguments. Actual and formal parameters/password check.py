# Declare a function named check_password that takes a string argument (password) and has one formal parameter
# chars with initial value as the string '$%!?@#'. The function should check if the password contains at least
# one character from chars and that the password length is at least 8 characters. If the test passes,
# then the function returns True, otherwise False.


def check_password(password, chars='$%!?@#'):
    flag = True
    counter = 0
    if len(password) > 8:
        for x in chars:
            if x in password:
                counter += 1
    else:
        flag = False

    return True if flag and counter != 0 else False


print(check_password(input("think up a password: ")))
