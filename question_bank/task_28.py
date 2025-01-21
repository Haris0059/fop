# Write a function to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.


def change(s):
    if s[-3:] == 'ing':
        s += 'ly'
    elif len(s) >= 3:
        s += 'ing'
    return s

print(change('abc')) # abcing
print(change('string')) # stringly