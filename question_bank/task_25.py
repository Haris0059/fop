# Write a function to return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceded by a period (.).
# So "xxyz" counts but "x.xyz" does not.

def xyz_there(s):
    for i in range(len(s)-2):
        if s[i:i+3] == 'xyz' and (i == 0 or s[i-1] != '.'):
            return True
    return False



print(xyz_there('abcxyz')) # True
print(xyz_there('abc.xyz')) # False
print(xyz_there('xyz.abc')) # True
