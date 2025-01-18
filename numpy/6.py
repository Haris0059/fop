# Write a Python function to remove consecutive duplicates of a given list.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

import numpy as np

def remove_duplicates(array):
    unique = np.array(array[array not in unique])
    return unique



sample = np.array([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
print(remove_duplicates(sample))