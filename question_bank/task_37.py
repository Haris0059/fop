# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
# Write a function

def near_ten(num):
    result = num % 5
    if result > 2:
        return False
    else:
        return True

print(near_ten(12)) # TRUE
print(near_ten(17)) # TRUE
print(near_ten(19)) # FALSE
