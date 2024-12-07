# Write a function that for a given dictionary (whose all values are integers)
# returns a dictionary in which all values are replaced by their rightmost digit
# (for example 29 is replaced by 9).

def rightmost_digit(dict):
    for (key, value) in dict.items():
        dict[key] = value%10
    return dict

sample = {
    'haris': 1,
    'ajla': 15,
    'edin': 6918,
    'selki': 15568
}
print(rightmost_digit(sample))