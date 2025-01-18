# write a docstring

def calculate_area(length, width):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return length * width

print(calculate_area(5,4).__doc__)