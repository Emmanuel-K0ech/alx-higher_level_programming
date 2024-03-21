#!/usr/bin/python3
""" Module 2-rectangle.py """


class Rectangle:
    """ Class definition
    Args
        width(int): dimension of rectangle
        height(int): demension of rectangle
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns area of rectacgle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates and returns perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))
