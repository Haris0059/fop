# Write a function to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def single(a,b):
    return b[:2] + a[-1] + ' ' + a[:2] + b[-1]

print(single('abc', 'xyz'))