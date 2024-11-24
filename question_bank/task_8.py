# Write a Python program to display the sign of the Chinese Zodiac for a given year in which you were born.
year = int(input("Enter a year which you were born: "))

for i in range(0,12):
    new = 1900 + i
    for j in range (1,12):
        if new == year:
            print("wow")
        new += 12


