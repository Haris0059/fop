# Write a Python function to find the item with maximum occurrences in a given list.
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list:
# 2

import numpy as np

def maximum_occurrences(array):
    unique = np.unique(array)
    computed_values = []

    for i in unique:
        occurrences = array[array == i]
        total_sum = sum(occurrences)
        computed_value = total_sum / i
        computed_values.append(computed_value)

    biggest = np.argmax(computed_values)
    return unique[biggest]


sample = np.array([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2])
print(maximum_occurrences(sample))