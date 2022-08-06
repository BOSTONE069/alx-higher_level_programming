#!/usr/bin/python3

from base import Base


class Rectangle(Base):
    """The is used to represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """
            It returns the width of the rectangle.
            :return: The width of the rectangle
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            It sets the width of the rectangle.
            :param value: The value to be assigned to the attribute
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """
            It returns the height of the rectangle.
            :return: The height of the rectangle
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            The function height() takes in a parameter called value
            and sets the value of the private variable __height to
            the value of the parameter

            :param value: The value to be assigned to the attribute
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """
            The function x() returns the value of the private variable __x
            :return: The value of the private variable __x
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            The function x() takes in two arguments, self and value,
            and sets the value of the variable x to the value of
            the argument value

            :param value: The value to be assigned to the attribute
            """
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """
            It returns the value of the private variable y.
            :return: The value of the y attribute.
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            The function y() takes in a value and checks if it is
            an integer and if it is greater than 0. If it is, it sets
            the value of y to the value passed in. If it is not, it raises an error

            param value: The value that is passed to the setter function
            """
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be > 0")
            self.__y = value
