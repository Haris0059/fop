# Write a Python function to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570

def convert(tup):
    string = ''
    for i in tup:
        string += str(i)
    return int(string)

print(convert((1,2,3))) # 123
print(convert((10,20,40,5,70))) # 102040570