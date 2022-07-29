
#TASK-1

#IMPORT REGULAR EXPRESSION:

import re

# CREAT EMAIL ID PATTERN:
def email():
    pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_id = input("ENTER YOUR EMAIL ID : ")
    if re.search(pattern, user_id):
        return ("VALID EMAIL ID")
    else:
         return("INVALID EMAIL ID")
x=email()
print(x)

#CREAT A PASSWORD PATTERN:
def password():
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    user_id = input("ENTER YOUR PASSWORD : ")
    if re.search(pattern, user_id):
        return ("VALID PASSWORD")
    else:
         return("INVALID PASSWORD")
x=password()
print(x)








