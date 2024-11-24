# Write a function to find the sum of numbers from 1 to n using recursion.

def findsum(num):
    if num == 1:
        return 1
    else:
        return num + findsum(num-1)


num = int(input("Enter a number: "))
print(findsum(num))1