# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

for i in range(0, m):
    print(" *", end="")
    for j in range(0, n-1):
        print(" *", end="")
    print("")