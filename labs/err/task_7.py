# Write a Python function splitList() to split a given list into two parts, where the length of the first part of the list
# is specified by the user. The function should handle the case where the specified length exceeds the length of the list
# or if the input is invalid (e.g., the length is not an integer). If an invalid length is provided,
# it should raise an exception and return an appropriate error message.
# splitList([1, 1, 2, 3, 4, 4, 5, 1], 3) → ([1, 1, 2], [3, 4, 4, 5, 1])
# splitList([1, 1, 2, 3, 4, 4, 5, 1], 10) → 'Error: Length exceeds list size'
# splitList([1, 1, 2, 3, 4, 4, 5, 1], -2) → 'Error: Invalid length'
# splitList([], 2) → 'Error: List is empty'

def splitList(lista, length):
    if len(lista) == 0:
        empty = 'Error: List is empty'
        raise TypeError(empty)
    if len(lista) <= length:
        list_size = 'Error: Length exceeds list size'
        raise TypeError(list_size)
    if length < 0:
        invalid_length = 'Error: Invalid length'
        raise TypeError(invalid_length)
    else:
        new = []
        new2 = []
        for i in range(len(lista)):
            if i >= length:
                new2.append(lista[i])
            else:
                new.append(lista[i])
        print(new, new2)

splitList([], 2)