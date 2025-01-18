# Write a Python function getListElement() that takes a list and an index as arguments.
# Use a try-except block to handle: IndexError when the index is out of bounds.
# A general except block for any other errors.
# getListElement([1, 2, 3], 5) → 'Index is out of range.'
# getListElement([1, 2, 3], 'a') → 'An error occurred.'
# getListElement([1, 2, 3], 1) → 2

def getListElement(lista, index):
    return lista[index]

try:
    #print(getListElement([1, 2, 3], 5))
    #print(getListElement([1, 2, 3], 'a'))
    print(getListElement([1, 2, 3], 1))
except IndexError as err:
    print(err, 'Index is out of range.')
except TypeError as err:
    print(err, 'An error occured.')