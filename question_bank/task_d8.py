# Write a Python function to get the maximum and minimum value in a dictionary.

def min_max(dict):
    max_dict = max(dict.values())
    min_dict = min(dict.values())
    return f'Min is {min_dict}, Max is: {max_dict}'

sample = {'1': 1, '2': 2, '3': 3}
print(min_max(sample))