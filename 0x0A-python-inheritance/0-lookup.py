#!/usr/bin/python3
""" 0-lookup.py module """


def lookup(obj):
    """ Returns a list of available attributes and methods of an object """
    obj_list = []
    obj_list =list(dir(obj))
    return obj_list
