#!/usr/bin/python3
"""writing a docstring"""
import math


class MagicClass:
    """setting up the magic"""

    def __init__(self, radii=0):
        """ Another docstring """
        self.__radii = 0
        if type(radii) is not int and type(radii) is not float:
            raise TypeError('radii must be a number')
        self.__radii = radii

    def area(self):
        """ Another docstring"""
        return self.__radii ** 2 * math.pi

    def circumference(self):
        """Another docstring"""
        return 2 * math.pi * self.__radii
