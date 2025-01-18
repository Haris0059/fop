def find_largest(numbers):
    largest = -100
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [-10, -20, -5, -15]
print("The largest number is:", find_largest(numbers))
