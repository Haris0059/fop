# Write a Python function cat_dog() that returns True if the string "cat" and the string "dog" appear the
# same number of times in the given string. The function should handle cases where the input is empty,
# and raise an exception if the input is not a string.
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True
# cat_dog('') → 'Error: Input string is empty'
# cat_dog(12345) → 'Error: Input must be a string'

def cat_dog(s):
    if type(s) is not str:
        string = 'Input must be a string'
        raise ValueError(string)
    if len(s) == 0:
        empty = 'Input string is empty'
        raise ValueError(empty)
    cat_count = s.count('cat')
    dog_count = s.count('dog')
    if dog_count == cat_count:
        return True
    else:
        return False

print(cat_dog(12345))