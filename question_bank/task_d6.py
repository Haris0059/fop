# Write a Python function to multiply all the values in a dictionary.

def multiply_all(dict):
    result = 1
    for i in dict.values():
        result *= i
    return result

sample = {'1': 1, '2': 2, '3': 3}
print(multiply_all(sample))