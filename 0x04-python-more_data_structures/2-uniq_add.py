#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for i in my_list:
        if i in new_list and i in my_list:
            continue
        else:
            new_list.append(i)
    for i in new_list:
        result += i
    return result
