# Write a function custom_mask_with_logic that takes a 1D NumPy array,
# a threshold, and a replacement value. The function should:
# Replace values greater than the threshold with their square.
# Replace values less than the threshold with the replacement value.
# Leave values equal to the threshold unchanged.

import numpy as np

def custom_mask_with_logic(array, threshold, replacement_value):
    array[array > threshold] = array[array > threshold]**2
    array[array < threshold] = replacement_value
    return array

sample = np.array([2,3,8])
print(custom_mask_with_logic(sample, 3, 100))