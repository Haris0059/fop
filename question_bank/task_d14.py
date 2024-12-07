# Write a Python function to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

def match(x, y):
    for key in x:
        if key in y and x[key] == y[key]:
            print(f'{key}: {x[key]} is present in both x and y')

sample1 = {'key1': 1, 'key2': 3, 'key3': 2}
sample2 = {'key1': 1, 'key2': 2}

match(sample1, sample2)