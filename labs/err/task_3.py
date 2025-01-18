# Write a Python function convertToInt() that takes a string as input and converts it to an integer.
# # Use a try-except block to handle a ValueError when the string cannot be converted. Include an else block to print a
# success message if the conversion is successful.
# convertToInt("123") → 'Conversion successful. Result: 123'
# convertToInt("abc") → 'Error: Cannot convert string to integer.'
# convertToInt("456") → 'Conversion successful. Result: 456'

def convertToInt(s):
    print(int(s), end=' ')

try:
    convertToInt('456')
except ValueError as err:
    print('Error: Cannot convert string to integer.')
else:
    print('Conversion successful.', end=' ')