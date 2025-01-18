# Write a Python function to reverse strings
# in a given list of string values.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

def reverse_list(list):
    new_list = []
    test = ""
    for i in list:
        new_list.append(reverse_string(i))
    return new_list

def reverse_string(word):
    new = ""
    for i in word:
        new = i + new
    return new



sample = ['Red', 'Green', 'Blue', 'White', 'Black']
print(reverse_list(sample))