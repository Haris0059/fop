# Write a Python function to get the total length of all values of a given dictionary with string values.
# Original dictionary:
# {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20

def counter(dict):
    counter = 0
    for value in dict.values():
            counter += len(value)
    return counter

sample = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
print(counter(sample))