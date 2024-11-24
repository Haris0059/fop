

def sum_of_digits(number):
    suma = 0
    if number <= 9:
        return number
    else:
        while number > 0:
            suma += number%10
            number //= 10
        return sum_of_digits(suma)
print(sum_of_digits(9875))