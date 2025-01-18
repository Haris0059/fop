# Write a Python function combineListsToDict() to combine two lists into a dictionary,
# where the elements of the first list serve as the keys and the elements of the second list serve as the values.
# The function should ensure that:
# The values of the first list are unique and hashable.
# The values in the second list are only integers.
# For each key, the value should be the sum of the corresponding value in the second list and the next value in the second list
# (i.e., value[i] + value[i+1]).
# Handle cases where the lists have different lengths, where the second list contains non-integer values, and where the
# first list contains non-unique or non-hashable values.
# combineListsToDict(['a', 'b', 'c'], [1, 2, 3, 4]) → {'a': 3, 'b': 5, 'c': 7, 'd': 9}
# combineListsToDict(['a', 'b', 'c', 'a'], [1, 2, 3]) → 'Error: Lists have different lengths'
# combineListsToDict([], [1, 2, 3]) → 'Error: First list is empty'
# combineListsToDict(['a', 'b'], []) → 'Error: Second list is empty'

def combineListsToDict(l1,l2):
    if len(l1)<=len(l2):
        different_lengths = 'Lists have different lengths'
        raise ValueError(different_lengths)
    if bool(l1):
        first_empty = 'First list is empty'
        raise ValueError(first_empty)
    if bool(l2):
        second_empty = 'Second list is empty'
        raise ValueError(second_empty)

    d = dict(zip(l1,changeList(l2)))
    print(d)

def changeList(l2):
    return [l2[i]+l2[i+1] for i in range(len(l2)-1)]


combineListsToDict(['a', 'b', 'c'], [1, 2, 3, 4])