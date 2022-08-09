#!/usr/bin/python3

# Importing the Base class from the base.py file.
from models.base import Base


class Rectangle(Base):
    """The is used to represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The constructor of the Rectangle class.

        :param width: width of the rectangle
        :param height: height of the rectangle
        :param x: x-axis position, defaults to 0 (optional)
        :param y: y-axis position, defaults to 0 (optional)
        :param id: the id of the rectangle
        """
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
        if type(value) != int:
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
        if type(value) != int:
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
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        The function area() takes in a rectangle
        object and returns the area of the rectangle
        :return: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        The function __str__() returns a string representation of the object
        :return: The id, x, y, width, and height of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        If args is not empty,
        then it will assign the first argument to id, the second to width, the third
        to height, the fourth to x, and the fifth to y. If kwargs is not empty, then
        it will assign the value of each key to the attribute of the same name.
        """
        a_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0 and len(kwargs) <= 5:
            for i, arg in enumerate(args):
                setattr(self, a_list[i], arg)
        if kwargs is not None and len(kwargs) > 0 and len(kwargs) <= 5:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        :return: A dictionary with the id, width, height, x, and y of the rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x":self.x, "y":self.y}