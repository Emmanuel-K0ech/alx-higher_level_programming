#!/usr/bin/python3
""" Module 9-rectangle.py """


class Rectangle:
    """ Class definition
    Args
        width(int): dimension of rectangle
        height(int): demension of rectangle
        number_of_instances(class attribute)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ string representation of an object """
        representation = ""
        if self.__width == 0 or self.__height == 0:
            return representation
        for x in range(self.__height):
            representation += str(self.print_symbol) * self.__width + "\n"
        return representation.strip()

    def __repr__(self):
        """ Returns official representation of the object """
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __del__(self):
        """ Deletes instance of the class """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ Compares area of rectangle and returns the largest """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_of_1 = rect_1.area()
        area_of_2 = rect_2.area()
        if area_of_1 > area_of_2:
            return rect_1
        elif area_of_2 > area_of_1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ Returns new Rectangle instance with width == height == size """
        return cls(width=size, height=size)
