#!/usr/bin/python3
""" This is a module to a class(square) """


class Square:
    """ This is a class with a private field and __init__ method """
    def __init__(self, size=0):
        """ initializes the following fields

            Args:
                __size: dimensions of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Getter func: Retrieves __size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter func: sets the value of __size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes the Area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Prints square using '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
