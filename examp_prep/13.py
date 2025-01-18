# modify function to accept optional greeting message

# Current code
def greet(name=None):
    if name == None:
        print('Hello, there!')
    else:
        print("Hello,", name, "!")

greet('Haris')