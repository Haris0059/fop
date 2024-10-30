# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If the speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2.
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# Write a function.

def caught_speeding(speed, birthday):
    no_ticket = 0
    small_ticket = 1
    big_ticket = 2
    if birthday == True:
        if 65 >= speed:
            print(no_ticket)
        elif 85 >= speed >= 66:
            print(small_ticket)
        elif speed >= 86:
            print(big_ticket)
    else:
        if 60 >= speed:
            print(no_ticket)
        elif 80 >= speed >= 61:
            print(small_ticket)
        elif speed >= 81:
            print(big_ticket)

caught_speeding(60, False)
caught_speeding(65, False)
caught_speeding(65, True)