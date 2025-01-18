# trace the value of the variable at each step

def mystery_function(n):
    result = 1
    print(result)
    for i in range(1, n + 1):
        result *= i
        print(result)
    return result

print(mystery_function(4))