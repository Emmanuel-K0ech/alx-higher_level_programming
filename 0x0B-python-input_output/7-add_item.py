#!/usr/bin/python3
import sys
import importlib


module_name1 = "5-save_to_json_file"
module_name2 = "6-load_from_json_file"
save_module = importlib.import_module(module_name1)
load_module = importlib.import_module(module_name2)
add_list = sys.argv[1:]
json_filename = "add_item.json"
with open(json_filename, 'a') as f:
    save_module.save_to_json_file(add_list, json_filename)
    my_obj = load_module.load_from_json_file(json_filename)
