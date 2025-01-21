def find_pairs(numbers, target):
    result = []
    length = len(numbers)
    for i in range(length):
        if numbers[i] + numbers[i] == target:
            result.append(tuple([numbers[i], numbers[i]]))
        if (i + 1) <= length:
            for j in range(i+1,length):
                print(numbers[i], numbers[j])
                if numbers[i] + numbers[j] == target:
                    result.append(tuple([numbers[i], numbers[j]]))
    return result

numbers = [2, 4, 3, 7, 5, -1, 8]
target_sum = 6
print(find_pairs(numbers,target_sum))
# Output: [(2, 4), (3, 3), (7, -1)]
