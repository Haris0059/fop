# Write a Python function divideNumbers() that takes two arguments, a numerator and a denominator, and returns their division.
# Implement a try-except block to handle the case where the denominator is zero.
# divideNumbers(10, 0) → 'Error: Cannot divide by zero'
# divideNumbers(10, 2) → 5.0

def divideNumbers(a,b):
    return round(a/b,1)

try:
    print(divideNumbers(10,2))
except ZeroDivisionError as err:
    print('Error: Cannot divide by zero')