#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        If the id is not None,
        then the id is set to the id passed in. If the id is None, then the id is set
        to the number of objects created so far plus one.

        param id: the id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

