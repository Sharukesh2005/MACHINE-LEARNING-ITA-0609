# Password Strength Checker

import string

password = input("Enter Password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch in string.punctuation:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("\nStrong Password")
else:
    print("\nWeak Password")
