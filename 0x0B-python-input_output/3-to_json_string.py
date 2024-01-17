#!/usr/bin/python3
"""The function below converts object to json string"""
import json


def to_json_string(my_obj):
    """
    Arg:
        my_obj: object to convert to JSON

    Return: JSON representation of obj(str)
    """
    json_str = json.dumps(my_obj)
    return json_str
