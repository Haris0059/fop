# Given two strings, write a function to return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.

def end_other(a,b):
    a = a.lower()
    b = b.lower()

    if a[-len(b):] == b or b[-len(a):] == a:
        print(True)
    else:
        print(False)

end_other('Hiabc', 'abc') # True
end_other('AbC', 'HiaBc') # True
end_other('abc', 'abXabc') # True