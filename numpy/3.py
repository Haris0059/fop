# Write a function double_diagonal_elements that takes a square 2D NumPy array
# (same number of rows and columns).
# The function should double all the elements on the main diagonal
# if they are even, and add 3 to them if they are odd.

import numpy as np

def double_diagonal_elements(array):
    length = len(array)
    for i in range(length):
        if array[i, i] % 2 == 0:
            array[i, i] *= 2
        else:
            array[i,i] += 3
    return array


sample = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
])

print(double_diagonal_elements(sample))