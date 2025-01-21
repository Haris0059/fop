# Write a function to find the first repeated character in a given string

def repeat(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return s[i]
    return False

print(repeat('harisesesees'))