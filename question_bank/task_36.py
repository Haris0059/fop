# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# Write a function.

def in1to10(n, outside_mode):
    if outside_mode is True:
        if 1 >= n or n >= 10:
            return True
    elif 10 >= n >= 1:
        return True
    else:
        return False

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))