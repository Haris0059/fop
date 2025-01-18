# Write a Python function checkKey() to check whether a given key already exists in a dictionary.
# The function should handle the case where the input dictionary is empty by raising a KeyError.
# If the key is not found in the dictionary, the function should return a message indicating that the key does not exist.
# checkKey({'name': 'Alice', 'age': 25}, 'age') → 'Key exists'
# checkKey({'name': 'Alice', 'age': 25}, 'address') → 'Key does not exist'
# checkKey({}, 'name') → 'Error: Dictionary is empty'

def checkKey(d, key):
    empty = bool(d)
    if empty:
        keys = [i for i in d.keys()]
        if key in keys:
            print('Key exists')
        else:
            print('Key does not exist')
    else:
        empty = 'Dictionary is empty'
        raise KeyError(empty)

#checkKey({'name': 'Alice', 'age': 25}, 'address')
checkKey({}, 'name')