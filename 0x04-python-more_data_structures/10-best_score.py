#!/usr/bin/python3
def best_score(a_dictionary):
    name = ""
    score = 0
    if a_dictionary is None or a_dictionary == {}:
        return None
    for k, v in a_dictionary.items():
        if v > score:
            name = k
            score = v
    return name
