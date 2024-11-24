# Write a Python program to find numbers between 100 and 400 (both included)
# where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence.
for i in range (100, 401):
    if i % 2 == 0:
        print (i, end=" ")
    else:
        pass