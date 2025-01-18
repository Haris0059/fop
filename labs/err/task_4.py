# Write a Python function alarm_clock() that takes a value for a day ( 0=Sun, 1=Mon, 2=Tue, ..., 6=Sat)
# and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring.
# Weekdays, the alarm should be "7:00", and on the weekend, it should be "10:00".
# If we are on vacation, then on weekdays the alarm should be "10:00", and on weekends it should be "off".
# The function should also include a try-except-finally block to catch any potential errors, such as invalid day values,
# and display an appropriate message.
# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'
#  alarm_clock(0, True) → 'off'
# alarm_clock(3, True) → '10:00'

def alarm_clock(day, vacation):
    if day > 6 or day < 0:
        invalid_day = ValueError(f'{day} is not valid number')
        raise invalid_day
    if vacation == True:
        if day > 0 and day < 6:
            print('10:00')
        elif day == 0 or day == 6:
            print('off')
    elif vacation == False:
        if day > 0 and day < 6:
            print('07:00')
        elif day == 0 or day == 6:
            print('10:00')
    else:
        invalid_value = TypeError(f'{vacation} is not correct Boolean value')
        raise invalid_value

try:
    alarm_clock(-1, False)
except NameError as err:
    print(err)
except TypeError as err:
    print(err)