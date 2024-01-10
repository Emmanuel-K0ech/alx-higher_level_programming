#!/usr/bin/python3
def read_file(filename=""):
    """
    Function read file
    filename:
        file to be read
    Returns:
        void
    """
    with open(filename) as f:
        print(f.read(), end="")
