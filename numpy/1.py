# Write a function replace_with_condition that takes a 2D NumPy array, a condition value,
# and a replacement value. The function should iterate over the array and replace all elements
# greater than the condition value with the replacement value.

import numpy as np

def replace_with_condition(array, condition_value, replacement_value):
    array[array > condition_value] = replacement_value
    return array

sample = np.array([[2, 3, 8], [5, 8, 9]])
print(replace_with_condition(sample, 3, 0))