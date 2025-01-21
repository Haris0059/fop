# Write a function to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def change(s):
    char = s[0]
    result = char
    for i in range(len(char), len(s)):
        if s[i] in char:
            result += '$'
        else:
            result += s[i]
    return result

print(change('restart'))