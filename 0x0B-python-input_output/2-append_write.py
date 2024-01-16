#!/usr/bin/python3
""" Function to append to a file """


def append_write(filename="", text=""):
    """
    Appends to a file and returns the number of characters added

        Arg:
            filename: file to append to
            text: chars to append

        Return: number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        written_text = f.write(text)
        return written_text
