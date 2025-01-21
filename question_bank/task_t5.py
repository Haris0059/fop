# Write a Python function to check if a specified element presents in a tuple of tuples.
# Original list: (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

def check(a):
    tup_of_tups = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
    for tup in tup_of_tups:
        if a in tup:
            return True
    return False

print(check('White')) # True
print(check('Olive')) # False