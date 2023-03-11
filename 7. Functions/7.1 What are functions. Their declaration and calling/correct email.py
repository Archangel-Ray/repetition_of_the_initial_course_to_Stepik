# Write a function that validates the email address passed to it as a string. We will assume that the address
# is correct if it necessarily contains the characters '@' and '.', and all other characters can take the values:
# 'a-z', 'A-Z', '0-9' and '_'. If the email is valid, then the function outputs YES, otherwise NO.
#
# After the function is declared, read (using the input function) the string containing the email address and call
# the function with that argument.


def verification_email(email):
    alphabet = ['_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '@', '.']
    flag = 'YES'
    if '@' in email:
        if '.' in email.split('@')[1]:
            for a in email:
                if a not in alphabet:
                    flag = 'NO'
                    break
        else:
            flag = 'NO'
    else:
        flag = 'NO'

    print(flag)


email_address = input('enter email address: ')
verification_email(email_address)
