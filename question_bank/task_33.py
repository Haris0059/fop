# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20. Write a function.

def sorta_sum(a, b):
    suma = 0
    suma = a + b
    if 20 >= suma >= 10:
        return 20
    return suma

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))