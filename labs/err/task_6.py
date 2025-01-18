# Write a Python function findItemIndex() to find the index of an item in a specified list.
# The function should handle the case where the item is not found in the list by using a try-except block.
# If the item is not found, it should return a message indicating that the item is not in the list.
# findItemIndex([1, 2, 3, 4, 5], 3) → 2
# findItemIndex([1, 2, 3, 4, 5], 6) → 'Item not found in the list'
# findItemIndex([], 3) → 'Item not found in the list'

def finditemInted(lista, index):
    try:
        return lista[index]
    except IndexError:
        return 'Item not found in the list'

print(finditemInted([], 6))