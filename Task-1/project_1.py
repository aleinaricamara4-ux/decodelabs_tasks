# create a program that checks whether a password is weak, medium, or strong.

import string

password = input("Enter your password: ")

score = 0

# check password length

if len(password) >= 8:
    score += 1

# check uppercase 
if any(char.isupper() for char in password):
    score += 1

# check numbers
if any(char.isdigit() for char in password):
    score += 1

# check symbols
if any(char in string.punctuation for char in password):
    score += 1


# display password strength
if score <= 1:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")


