# Write a Python function to create a list of all the keys in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']

def flat(dict):
    list = []
    for key in dict:
        list.append(key)
    return list

sample = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
print(flat(sample))