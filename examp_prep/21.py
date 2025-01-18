def tuples_to_dict(tuple_list):
    result = {}

    for (key,value) in tuple_list:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

tuple_list = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]
print(tuples_to_dict(tuple_list))
# Output: {'a': [1, 3], 'b': [2, 5], 'c': [4]}
