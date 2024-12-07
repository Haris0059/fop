# Write a Python function to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: ('S005', 'S002', 'S007', 'S001', 'S009')

def unique(list):
    unique_list = []
    for i in list:
        for (key,value) in i.items():
            if value in unique_list:
                pass
            else:
                unique_list.append(value)
    return unique_list


sample = [
    {"V":"S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII":"S005"},
    {"V":"S009"},
    {"VIII":"S007"}
]

print(unique(sample))