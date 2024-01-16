#!/usr/bin/python3
""" The function writes a string to a text file """


def write_file(filename="", text=""):
    """
    Writes to a file and returns num of char written

        Arg:
            filename: file to write
            text: text to  write on file
        Return:
            number of char written
    """
    with open(filename, 'w') as f:
        written_char = f.write(text)
        return written_char
