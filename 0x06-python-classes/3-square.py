#!/usr/bin/python3
""" This is a module to a class(square) """


class Square:
    """ This is a class with a private field and __init__ method """
    def __init__(self, size=0):
        """ initializes the following fields

            Args:
                __size: dimensions of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Computes the Area of the square """
        return self.__size ** 2
