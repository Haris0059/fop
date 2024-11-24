# Write a function to reverse a string using recursion.

def reverse(string):
    if len(string) <= 1:
        return string
    else:
        return reverse(string[1:]) + string[0]


string = str(input("Enter a string: "))
print(reverse(string))