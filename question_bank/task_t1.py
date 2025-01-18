# Write a Python function to calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648

def calculate_product(tup):
    product = 1
    for i in tup:
        product *= i
    return product

tupla = (4, 3, 2, 2, -1, 18)
print(calculate_product(tupla))
