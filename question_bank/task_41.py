# For this problem,
# we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
# so 15 rounds up to 20.
# Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
# Write a function that for given 3 ints, a b c, returns the sum of their rounded values.

def suma(a, b, c):
    result = rounding(a) + rounding(b) + rounding(c)
    return result

def rounding(number):

    if number % 10 >= 5:
        return (number // 10 + 1) * 10
    else:
        return (number // 10) * 10


print(suma(16, 17, 18)) # 60
print(suma(12, 13, 14)) # 30
print(suma(6, 4, 4)) # 10
