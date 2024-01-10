#!/usr/bin/python3
"""
Function that reads a text file and prints to stdout
"""
def read_file(filename=""):
    with open(filename) as f:
        print(f.read(), end="")
