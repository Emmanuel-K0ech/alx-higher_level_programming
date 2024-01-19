#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers
    Checks whether the digits are integers
    Raises a TypeError if not

    Args:
        a(int): First integer
        b(int): Second integer defalut=98 if not keyed in

    Returns: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
