#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    denom = 0
    nume = 0
    for i in range(len(my_list)):
        nume += my_list[i][0] * my_list[i][1]
        denom += my_list[i][1]
    return nume / denom
