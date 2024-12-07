# Write a Python function to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

def filter(dict):
    list = []
    for (key, value) in dict.items():
        for i in value:
            if i % 2 == 0:
                list.append(i)
                dict[key] = list
        list = []
    return dict

sample = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
print(filter(sample))