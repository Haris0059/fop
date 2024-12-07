# Write a Python function to remove a key from a dictionary.

def remove_key(dict, key):
    del dict[key]
    return 'Done'

sample = {
    'name': 'haris',
    'surename': 'skeledzija',
    'age': 18,
    'uni': True
}

print(remove_key(sample, 'name'))
print(sample)