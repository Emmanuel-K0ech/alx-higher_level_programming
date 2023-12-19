#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    msg = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
    except ValueError:
        print("{}".format(msg), file=sys.stderr)
        return False
    return True
