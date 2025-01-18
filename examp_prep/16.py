# Write a function that takes a list of strings and returns a
# dictionary where the keys are word lengths and the values
# are lists of words of that length.
# from question_bank.task_d10 import unique

def group_words_by_length(words):
    result = {}
    for word in words:
        if len(word) not in result.keys():
            result[len(word)] = []
        result[len(word)].append(word)
    return result




words = ["apple", "banana", "pear", "kiwi", "peach", "cherry"]
print(group_words_by_length(words))
#Output: {5: ['apple', 'peach'], 6: ['banana', 'cherry'], 4: ['pear', 'kiwi']}
