# Write a Python function to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


def combine(d1, d2):
    new = d1.copy()
    for (key, value) in d2.items():
            if key in new.keys():
                new[key] += value
            else:
                new[key] = value
    return new

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(combine(d1,d2))