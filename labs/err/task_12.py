# Write a Python function sumTupleElements() to compute the sum of all the elements of each tuple stored inside a list of tuples. The function should handle cases where:
# The list is empty, raising an appropriate exception.
# The tuples contain non-numeric values, raising an exception.
# sumTupleElements([(1, 2), (2, 3), (3, 4)]) → [3, 5, 7]
# sumTupleElements([(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]) → [9, -1, 7, 8]
# sumTupleElements([]) → 'Error: List is empty'
# sumTupleElements([(1, 2), ('a', 3), (3, 4)]) → 'Error: Non-numeric values found in tuple'

def sumTupleElements(lista):
    if len(lista) == 0:
        empty = 'List is empty'
        raise ValueError(empty)
    l = []
    for tup in lista:
        suma = 0
        for i in tup:
            if type(i) is not int:
                non_numeric = 'Non-numeric values found in tuple'
                raise ValueError(non_numeric)
            suma += i
        l.append(suma)
    return l

print(sumTupleElements([(1, 2), ('a', 3), (3, 4)]))