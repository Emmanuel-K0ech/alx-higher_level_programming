#!/usr/bin/python3
"""
    Function returns an object
    from JSON representation string
"""
import json


def from_json_string(my_str):
    """
    Arg:
        my_str: JSON string to convert to object

    Return: object for JSON string
    """
    my_obj = json.loads(my_str)
    return my_obj
