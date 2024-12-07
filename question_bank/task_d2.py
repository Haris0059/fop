# Write a Python function to check whether a given key already exists in a dictionary.

def checker(dict, key):
    for i in dict.keys():
        if key == i:
            return True


dict = { 'haris':'test', 'ajla':'test2'}

print(checker(dict, 'ajla'))