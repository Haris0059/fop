converted = 0
weight = int(input("Enter your weight: "))
metric = str(input("(L)bs or (K)g: "))

if (metric == "L" or metric == "l"):
    converted = weight // 2.205
    print (f'You are {converted} Kg')
    
elif (metric == "K" or metric == "k"):
    converted = weight * 2.205
    print (f'You are {converted} Lbs')
    