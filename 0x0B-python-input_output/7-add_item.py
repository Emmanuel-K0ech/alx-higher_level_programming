#!/usr/bin/python3
"""
    The script adds all arguments to a python list by:
        copying the arguments from Args to a list[]
        get JSON representation using save_to_json_file()
        create obj using load_from_json_file()
"""
import sys
import importlib


module_name1 = "5-save_to_json_file"
module_name2 = "6-load_from_json_file"
save_module = importlib.import_module(module_name1)
load_module = importlib.import_module(module_name2)
new_args = []
new_args = sys.argv[1:]
json_filename = "add_item.json"
with open(json_filename, 'a') as f:
    save_module.save_to_json_file(new_args, json_filename)
    my_obj = load_module.load_from_json_file(json_filename)
