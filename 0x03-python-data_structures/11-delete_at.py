#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    new_list = []
    for i in range(0, len(my_list)):
        if i == idx:
            continue
        else:
            new_list.append(my_list[i])
    my_list.clear()
    for i in new_list:
        my_list.append(i)
    return new_list
