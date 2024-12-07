# Write a Python function to remove spaces from dictionary keys.

def remove_spaces(dict):
    new = {}
    for (key, value) in dict.items():
        new[key.replace(' ', '')] = value
    return new

sample = {
    'haris je': 1,
    'ha ha ha': 3,
    'lolllll': 5
}
print(remove_spaces(sample))