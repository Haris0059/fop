# Write a Python function to combine two lists into a dictionary, where the elements of the first one serve as the keys and the elements of the second one serve as the values. The values of the first list need to be unique and hashable.
# Sample Output:
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def combine(list1, list2):
    dict = {}
    counter = 0
    for i in list1:
        for j in range(0, len(list2)):
            if j == counter:
                dict[i] = list2[j]
                counter += 1
                break
    return dict

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5]
print(combine(list1, list2))