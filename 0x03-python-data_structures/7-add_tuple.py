#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    if len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) == 1:
        tuple_a = tuple_a + (0,)
        add_tuple(tuple_a=(), tuple_b=())
    elif len(tuple_b) == 1:
        tuple_b = tuple_b + (0,)
        add_tuple(tuple_a=(), tuple_b=())
    elif tuple_a == () and tuple_b == ():
        return None
    result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return result
