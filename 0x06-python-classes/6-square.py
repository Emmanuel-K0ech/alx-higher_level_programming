#!/usr/bin/python3
""" This is a module to class Square """


class Square:
    """ This is a class with a private field and __init__ method """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes the following fields

            Args:
                __size: dimensions of the square
                __position: positive integer tuple
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter func: Retrieves __size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter func: sets the value of __size

            Args:
                value: size input

            Check instance of value to validate input
            Assign value to size if all criterias are met
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter function that retrieves position(0, 0)"""
        return self.__position

    @position.setter
    def position(self, pos):
        """Validating the values in the tuple

            Args:
                pos: positonal tuple input

            Validate input of the pos tuple
            Assign pos to position
        """
        for x in pos:
            if not (x >= 0 and isinstance(x, int)):
                raise TypeError("position must be a tuple
                                of 2 positive integers")
            else:
                self.__position = pos

    def area(self):
        """ Computes the Area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Prints square using '#'
            The position(x, y) determine the underscores vertically
            and horizintally on the ## squares
        """
        for x in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)