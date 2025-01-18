def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrome("racecar"))  # Expected: True
print(is_palindrome("hello"))    # Expected: False
