def merge_dictionaries(dict1, dict2):
    result, unique = {}, []
    for i in dict1.keys():
        result[i] = dict1[i]
        unique.append(i)
        for j in dict2.keys():
            if i == j:
                result[i] += dict2[j]
            if j not in unique:
                result[j] = dict2[j]
    return result

dict1 = {'a': 5, 'b': 3, 'c': 8}
dict2 = {'b': 7, 'c': 2, 'd': 6}
print(merge_dictionaries(dict1,dict2))
# Output: {'a': 5, 'b': 10, 'c': 10, 'd': 6}
