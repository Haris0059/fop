# Write a Python function to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_num(list):
    counter = 0
    for i in list:
        if len(i) >= 3 and i[0] == i[-1]:
            counter +=1
    return counter

sample = ['abc', 'xyz', 'aba', '1221'] # 2

print(count_num(sample))