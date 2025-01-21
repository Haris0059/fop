# Write a Python function to convert a given list of tuples to a list of lists.

def convert(list_tups):
    result = []
    for tup in list_tups:
        result.append(list(tup))
    return result

print(convert([(1, 2), (2, 3), (3, 4)])) # [[1, 2], [2, 3], [3, 4]]
print(convert([(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)])) # [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]