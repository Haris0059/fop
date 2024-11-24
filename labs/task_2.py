# Write a function to set a number to the power using recursion.

def power(num):
    if num == 0:
        return 1
    else:
        return 2 * power(num-1)

print(power(3))