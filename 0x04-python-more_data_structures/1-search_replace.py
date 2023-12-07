#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_list = []
    for i in my_list:
        if i == search:
            result_list.append(replace)
        else:
            result_list.append(i)
    return result_list
