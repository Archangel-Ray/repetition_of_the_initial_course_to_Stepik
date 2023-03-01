# Enter a string with a phone number. Input format expected:
#
# +7(xxx)xxx-xx-xx
#
# where x is a digit. The size of the entered characters is considered correct
# (that is, it cannot be that any digit is missing or is superfluous).
# You need to check that the entered string conforms to this format.
# Print YES if it matches and NO otherwise.

phone = input('enter the phone according to the pattern - +7(xxx)xxx-xx-xx : ')
template = '+7(xxx)xxx-xx-xx'
flag = 'YES'
if len(phone) == len(template):
    for x in range(len(template)):
        if phone[x] == template[x]:
            continue
        elif template[x] == 'x':
            if not phone[x].isdigit():
                flag = 'NO'
                break
        else:
            flag = 'NO'
            break
else:
    flag = 'NO'
print(flag)
