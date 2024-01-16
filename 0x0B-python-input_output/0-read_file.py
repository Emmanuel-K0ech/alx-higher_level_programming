#!/usr/bin/python3
"""Function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """
    This is a read file function

    Arg:
        filename: name of file to read
    """
    with open(filename) as f:
        print(f.read(), end="")
