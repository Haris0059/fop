# Write a program that will continuously ask users to enter numbers. Once user types “done”,
# the program should stop asking for more numbers and display the sum of all the numbers that user entered.
total_sum = 0

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input.lower() == "done":
        break
    elif user_input.replace('.', '', 1).isdigit():  # Check if it's a number (including floats)
        total_sum += int(user_input)
    else:
        print("That's not a valid number. Please try again.")

print("The sum of all entered numbers is:", total_sum)
