#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_int = int(value)
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True
