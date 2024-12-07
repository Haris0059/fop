# Write a Python function to sum all the values in a dictionary.

def sum_all(dict):
    suma = 0
    for i in dict.values():
        suma += i
    return suma

sample = {'1': 1, '2': 2, '3': 3}
print(sum_all(sample))