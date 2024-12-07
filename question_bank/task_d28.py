# Write a function that for a given dictionary (whose all values are integers)
# returns a dictionary in which all values smaller than 14 are doubled.

def doubled(dict):
    for (key, value) in dict.items():
        if value < 14:
            dict[key] = value*value
    return dict


sample = {
    'haris': 1,
    'ajla': 5,
    'edin': 6918,
    'selki': 15568
}
print(doubled(sample))