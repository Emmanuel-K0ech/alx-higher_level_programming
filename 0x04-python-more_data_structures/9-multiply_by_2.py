#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res_dict = {}
    for k, v in a_dictionary.items():
        res_dict[k] = v * 2
    return res_dict
