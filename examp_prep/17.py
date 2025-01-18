def most_common_character(text):
    unique, highest = [], 0
    for i in text:
        if i not in unique:
            unique.append(i)

    for letter in unique:
        num = text.count(letter)
        if num > highest:
            highest = num
            result = [letter]
        elif num == highest:
            result.append(letter)
    return tuple(result)

text = "mississippi" # Output: ('i', 's')
print(most_common_character(text))