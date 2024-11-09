# Write a Python program that accepts a word from the user and reverse it.

word = str(input("Enter your word: "))
new_word = ""

for i in word:
    new_word = i + new_word
print(new_word)