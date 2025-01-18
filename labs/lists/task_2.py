# Write a function that will remove even numbers from a list and return a list with odd numbers.

def remove_even(list):
    return [i for i in list if i % 2 != 0]


numbers = [1, 2, 3, 4, 5, 6]
print(remove_even(numbers))