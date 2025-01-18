# Write a function to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

import numpy as np

def first_appearance(string):
    groups = string.split(' ')
    print(groups)
    for i in range(len(groups)):
        if groups[i] == 'not':
            for j in range(i+1, len(groups)):
                if groups[j] == 'poor'

print(first_appearance('The lyrics is not that poor!'))
print(first_appearance('The lyrics is poor!'))