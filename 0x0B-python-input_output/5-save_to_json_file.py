#!/usr/bin/python3
"""Function writes an object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    Arg:
        my_obj: object to write in file
        filename: file to write on

    The function uses the json.dump() method to write to file
    """
    with open(filename, 'a') as f:
        json.dump(my_obj, f)
