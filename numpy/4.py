# Write a function generate_checkerboard that takes two integers, rows and cols,
# as arguments and creates a 2D NumPy array filled with 1s and 0s in a checkerboard pattern
# (1 at even indices, 0 at odd indices).

import numpy as np

def generate_checkerboard(rows, cols):
    indices = np.indices((rows, cols))  # Pass dimensions as a tuple
    return (indices[0] + indices[1]) % 2  # Generate the checkerboard pattern

# Example usage
print(generate_checkerboard(4, 5))
