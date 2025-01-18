# Write a Python function left2() to return a "rotated left 2" version of a given string, where the first 2 characters are moved to the end.
# The string length will be at least 2.The function should include a check to ensure the input is a string and raise an exception if it is not.
# If the input string has fewer than 2 characters (which the task guarantees won't happen, but it's good practice), an appropriate error message
# should be raised.
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'
# left2(123) → 'Error: Input must be a string'
# left2('') → 'Error: Input string is empty'

def left2(s):
    if type(s) is not str:
        string = 'Input must be a string'
        raise ValueError(string)
    if len(s) == 0:
        empty = 'Input string is empty'
        raise ValueError(empty)
    if len(s) < 2:
        too_small_length = 'Length of the string is too small'
        raise ValueError(too_small_length)
    return s[2:] + s[0:2]

print(left2(123))