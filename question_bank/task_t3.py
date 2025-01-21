# Write a Python function to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

def convert(tup):
    new = []
    for i in tup:
        inside = []
        for j in i:
            inside.append(int(j))
        new.append(tuple(inside))
    return tuple(new)

tup = (('333', '33'), ('1416', '55'))
print(convert(tup))