#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    n = len(roman_string)

    for i in range(n):
        val = d.get(roman_string[i], 0)
        if i + 1 < n and val < d.get(roman_string[i + 1], 0):
            total -= val
        else:
            total += val
    return total
