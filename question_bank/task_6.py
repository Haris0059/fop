# Write a Python program to check the validity of password input by users.
#
#
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = str(input("Enter your password: "))

if len(password) < 6:
    print("Password is too short")
elif len(password) > 16:
    print("Password is too long")
