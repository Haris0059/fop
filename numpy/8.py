# Write a function to find maximum length of consecutive 0’s in
# given binary string.
# max_consecutive_0('111000010000110’) -> 4
# max_consecutive_0('111000111') -> 3

import numpy as np

def max_consecutives(string, target):
    if target == '1':
        groups = np.array(string.split('0'))
    else:
        groups = np.array(string.split('1'))
    length = np.vectorize(len)
    return max(length(groups))


print(max_consecutives('111000010000110', '0'))
print(max_consecutives('111000111', '0'))