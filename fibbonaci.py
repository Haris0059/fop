# fibbonacijev niz preko while petlje
# input: 5
# output: 1 1 2 3 5

counter = 0
a = 0
b = 1

number = int(input("enter your number: "))

while counter < number:
    temp = a
    a = b
    b += temp
    print(a, end=' ')
    counter += 1