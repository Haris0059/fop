# Write a Python function to change the position
# of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

def change_pos(list):
    for i in range(0, len(list) - 1,2):
        list[i], list[i+1] = list[i+1], list[i]
    return list

sample = [0,1,2,3,4,5]
print(change_pos(sample))