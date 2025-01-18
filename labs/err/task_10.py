# Write a Python function tupleToInt() to convert a given tuple of positive integers into a single integer.
# The function should handle cases where the tuple contains non-positive integers or is empty by raising appropriate exceptions.
# It should check that all elements in the tuple are positive integers and then concatenate them to form an integer.
# tupleToInt((1, 2, 3)) → 123
# tupleToInt((10, 20, 40, 5, 70)) → 102040570
# tupleToInt((1, -2, 3)) → 'Error: Tuple contains non-positive integers'
# tupleToInt(()) → 'Error: Tuple is empty'

def tupleToInt(t):
    if not bool(t):
        empty = 'Tuple is empty'
        raise ValueError(empty)
    else:
        s = ""
        for i in t:
            if i < 0:
                negative = 'Tuple contains non positive integers'
                raise TypeError(negative)
            else:
                s += str(i)
        print(int(s))

tupleToInt(())