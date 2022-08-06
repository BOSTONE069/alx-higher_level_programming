#!/usr/bin/python3

# It imports the class Rectangle from the file rectangle.py
from rectangle import Rectangle


class Square(Rectangle):
    """This represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        The __init__ function is a constructor that
        initializes the attributes of the class Square

        :param size: the size of the square
        :param x: x-coordinate of the top left corner of the square, defaults to 0 (optional)
        :param y: y-coordinate of the square, defaults to 0 (optional)
        :param id: The id of the object
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The __str__ method returns a string representation of the object
        :return: The id, x, y, and size of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        It returns the width of the rectangle.
        :return: The width of the rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        The function size() takes two arguments, self and value,
        and sets the width and height of the rectangle to value

        :param value: The value of the parameter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        If args is not empty,
        then it will assign the first argument to id, the second to size, the third
        to x, and the fourth to y. If kwargs is not empty, then it will assign the
        value of each key to the corresponding attribute.
        """
        a_list = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0 and len(kwargs) <= 5:
            for i, arg in enumerate(args):
                setattr(self, a_list[i], arg)
        if kwargs is not None and len(kwargs) > 0 and len(kwargs) <= 5:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of a Rectangle instance
        :return: A dictionary with the id, size, x, and y of the square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
