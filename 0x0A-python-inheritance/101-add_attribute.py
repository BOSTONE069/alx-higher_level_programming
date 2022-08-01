#!/usr/bin/python3


def add_attribute(obj, name, value):
    """function that adds a new attribute to an object if it’s possible """

    for element in dir(obj):
        if element == '__dict__':
            setattr(obj, name, value)
            return
    raise TypeError("can't add new attribute")

    # try:
    #     self.name = value
    # except:
    #     raise TypeError("can't add new attribute")
