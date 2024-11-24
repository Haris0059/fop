# Write a function to count down (print numbers in reverse order)
# starting with a specific number using recursion.

def countdown(num):
    if num == 0:
        print(0)
    else:
        print(num)
        countdown(num-1)

num = int(input("Enter a number: "))
countdown(num)