# Write a function blackjack that for  2 int values greater than 0,
# returns whichever value is nearest to 21 without going over. Return 0 if they both go over.

def blackjack(a, b):
    max = 21
    if a > max:
        a = 0
    if b > max:
        b = 0
    if a > b:
        return a
    else:
        return b

print(blackjack(19, 21)) # 21
print(blackjack(21, 19)) # 21
print(blackjack(19, 22)) # 19