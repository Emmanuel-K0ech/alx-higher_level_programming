#!/usr/bin/python3
"""Function creates object from file with JSON data of the obj"""
import json


def load_from_json_file(filename):
    """
    Arg:
        filename: file to create obj from

    Return: obj created
    """
    with open(filename, 'r') as f:
        my_obj = json.load(f)
        return my_obj
