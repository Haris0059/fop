# Write a function to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def lyrics(s):
    not_index = s.find('not')
    poor_index = s.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        s = s[:not_index] + 'good' + s[poor_index + 4:]
    return s
print(lyrics('The lyrics is not that poor!')) # 'The lyrics is good!'
print(lyrics('The lyrics is poor!')) # 'The lyrics is poor!'