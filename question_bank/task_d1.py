#  Write a Python function to concatenate the three dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concatenate_dict(first, second, third):
    new = {**first, **second, **third}
    return new
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

print(concatenate_dict(dic1, dic2, dic3))