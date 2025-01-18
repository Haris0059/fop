
def find_largest(list):
    list.sort()
    return list[-1]

numbers = [1, 2, 3, 6, 5, 1]
print(find_largest(numbers))