#!/usr/bin/python3

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
