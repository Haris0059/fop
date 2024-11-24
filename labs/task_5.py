# Write a function to count the number of digits in a positive integer using recursion.

def counter(num):
    if num // 10 == 0:
        return 1
    else:
        return 1 + counter(num // 10)


num = int(input("Enter a number: "))
print(counter(num))