# Write a Python function checkElementInTuple() to check if a specified element is present in a tuple of tuples.
# The function should handle cases where the element is not found in any of the sub-tuples or if the input is not a tuple of tuples,
# raising appropriate exceptions.
# checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'White') → True
# checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'Olive') → False
# checkElementInTuple([], 'White') → 'Error: Input is not a tuple of tuples'
# checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple')), 5) → 'Error: Element is not a string'

def checkElementInTuple(t, flag):
    if type(t) is not tuple:
        not_tuple = 'Input is not a tuple of tuples'
        raise ValueError(not_tuple)
    if type(flag) is not str:
        not_str = 'Element is not a string'
        raise ValueError(not_str)
    works = False
    for tup in t:
        for word in tup:
            if word == flag:
                works = True
                return True
        if not works:
            return False



print(checkElementInTuple((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple')), 5))