# Write a Python function to iterate over dictionaries using for loops.

def iterate(dict):
    for (key, value) in dict.items():
        print(f'{key}: {value}')

sample = {
    'name': 'haris',
    'surename': 'skeledzija',
    'age': 18,
    'uni': True
}

iterate(sample)