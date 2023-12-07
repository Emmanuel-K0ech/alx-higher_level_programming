#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dictionary = {
            'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1
            }
    num = 0
    temp = 0
    roman_value = []
    for i in list(roman_string):
        roman_value.append(roman_dictionary[i])
    for i in range(len(roman_value)):
        if i == 0:
            num += roman_value[i]
            temp = roman_value[i]
        else:
            if temp < roman_value[i]:
                num += roman_value[i]
                temp = roman_value[i]
            elif temp > roman_value[i]:
                num += roman_value[i]
                temp = roman_value[i]
    return num
