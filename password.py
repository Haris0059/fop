import string
import math

def generate_password(pattern):
    password = ""
    for i in pattern:
        if i == "L":
            password += string.ascii_lowercase[0]
        elif i == "U":
            password += string.ascii_uppercase[-1]
        elif i == "D":
            password += string.digits[2]
        elif i == "S":
            password += string.punctuation[4]
        elif i == "H":
            password += string.ascii_letters[19]
    return password

def evaluate_password(password):
    score = counter = 0
    lower = upper = digits = special = False

    for i in password:
        if i in string.ascii_lowercase:
            score += 1
            if not lower:
                lower = True
                counter += 1
        elif i in string.ascii_uppercase:
            score += 2
            if not upper:
                upper = True
                counter += 1
        elif i in string.digits:
            score += 3
            if not digits:
                digits = True
                counter += 1
        elif i in string.punctuation:
            score += 4
            if not special:
                special = True
                counter += 1

    entropy = len(password) * math.log2(counter)
    return f"Score: {score}. Entropy: {entropy}."

password = generate_password("LUDSLL")
score = evaluate_password(password)

print(password)
print(score)