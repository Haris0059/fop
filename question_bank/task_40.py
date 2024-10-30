# Write a function that for given three integers, a b c,
# return true if it is possible to add two of them to get the third.

def twoAsOne(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return True
    else:
        return False

print(twoAsOne(1, 2, 3))
print(twoAsOne(3, 1, 2))
print(twoAsOne(3, 2, 2))