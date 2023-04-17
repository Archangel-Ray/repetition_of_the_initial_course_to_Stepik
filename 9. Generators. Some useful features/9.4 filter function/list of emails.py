# Enter a list of email addresses in one line separated by a space. Among them, you need to leave only correctly
# recorded addresses. We will assume that these include those that use Latin letters, numbers and the underscore
# character. And also in the address there must be an '@' symbol, and after it a dot symbol '.' (there may be other
# symbols in between, of course).
#
# Display the result as a string of email addresses separated by spaces.


def checking_email(email):
    flag = True
    if '@' in email:
        name_domain = email.split('@')
        if '.' in name_domain[1]:
            for i in email:
                if i not in '@.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_':
                    flag = False
                    break
        else:
            flag = False
    else:
        flag = False
    return flag


list_emails = input("if not laziness, write a few email addresses. otherwise - press enter: ").split()
if list_emails == []:
    list_emails = ['abc@it.ru', 'dfd3.ru@mail', 'biba123@list.ru', 'sc_lib@list.ru', '$fg9@fd.com']
correct_email = list(filter(checking_email, list_emails))
print(*correct_email)
