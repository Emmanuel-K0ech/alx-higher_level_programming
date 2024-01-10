#!/usr/bin/python3
import json


def from_json_string(my_str):
    my_obj = json.loads(my_str)
    return my_obj
