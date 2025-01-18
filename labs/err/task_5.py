# Write a Python function replaceChars() to get a string from a given string where all occurrences of its first character
# have been changed to $, except the first character itself.
# The function should handle the case where the input is not a string by using an exception block,
# raising an appropriate error message if the input is not a string.
# replaceChars('restart') → 'resta$t'
# replaceChars('ehello') → 'eh$llo'
# replaceChars(12345) → 'Error: Input must be a string'

def replaceChars(s):
    try:
        flag = s[0]
        print(flag + s[1:].replace(flag, '$'))
    except TypeError as err:
        print('Error: Input must be a string')


replaceChars('restartrrrrrrrrrrr')