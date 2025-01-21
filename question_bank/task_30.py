# Write a function to find the first non-repeating character in a given string.

def first_non(s):
    unique = []
    for char in s:
        if char not in unique:
            unique.append(char)
    for char in unique:
        counter = s.count(char)
        if counter == 1:
            return char

print(first_non('hhhhhhaaaaariiiissss'))