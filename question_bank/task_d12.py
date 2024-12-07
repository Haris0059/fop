# Write a Python function to combine values in a python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

def combine_values(list):
    new = {}
    for dict in list:
        item = dict['item']
        amount = dict['amount']
        if item in new:
            new[item] += amount
        else:
            new[item] = amount
    return new

sample = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]
print(combine_values(sample))