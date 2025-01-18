# Write a Python function that takes two lists
# and returns True if they have at least
# one common member.

def common_members(first, second):
    for i in first:
        for j in second:
            if i == j:
                return True

sample1 = [6,9,0,1,10]
sample2 = [1,2,3,4,5]

print(common_members(sample1, sample2))
