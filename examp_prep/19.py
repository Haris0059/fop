def flatten_list(nested_list):
    result = []
    for i in nested_list:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result


nested_list = [[1, 2], [3, [4, 5]], 6]
print(flatten_list(nested_list))
# Output: [1, 2, 3, 4, 5, 6]
