# Write a Python function to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

def display_combinations(dict):
    result = ['']

    for key in dict.keys():
        new_result = []
        for combination in result:
            for letter in dict[key]:
                new_result.append(combination + letter)
        result = new_result

    for combination in result:
        print(combination)

sample = {'1':['a','b'], '2':['c','d']}
display_combinations(sample)