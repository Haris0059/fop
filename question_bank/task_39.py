# Given 3 int values, a b c, write a function to return their sum.
# However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
# So for example, is 13, then botif b h b and c do not count.

def lucky_sum(a, b, c):
    result = 0
    if a == 13:
        return result
    elif b == 13:
        result = a
        return result
    elif c == 13:
        result = a + b
        return result
    else:
        result = a + b + c
        return result
print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))
