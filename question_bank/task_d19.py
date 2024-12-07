# Write a Python function to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

def max_key_for_value(dict):
    list = []
    for key in dict:
        if dict[key] == max(dict.values()) or dict[key] == min(dict.values()):
            list.append(key)
    return list

sample = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
print(max_key_for_value(sample))