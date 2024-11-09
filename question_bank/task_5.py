# Write a Python program that accepts a string and calculate the number of digits and letters.

string = str(input("Enter your word: "))
result = 0
for i in string:
    result += 1
print("There is", result, "letters!")