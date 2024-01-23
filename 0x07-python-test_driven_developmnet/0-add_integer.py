#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers
    Checks whether the digits are integers
    Raises a TypeError if not

    Args:
        a(int): First integer
        b(int, optional): Second integer defalut=98 if not keyed in

    Returns:
        int: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
