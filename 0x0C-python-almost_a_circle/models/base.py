#!/usr/bin/python3
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function converts a list of dictionaries to a JSON string.

        :param list_dictionaries: a list of dictionaries
        :return: A JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        It writes a list of dictionaries to a file

        :param cls: the class that we're calling the method from
        :param list_objs: a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        It takes a json string and returns a python object.

        :param json_string: the string to be converted
        :return: A list of JSON string representation.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        If the dictionary is not empty, create a new
        instance of the class, update the
        attributes of the new instance, and
        return the new instance.

        :param cls: the class that is calling the function
        :return: A new instance of the class with the attributes updated
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        "If the file exists,
        read it and return a list of instances created from the file's JSON string.
        Otherwise, return an empty list."

        The first line of the function creates the filename from the class name.
        The try/except block attempts to open the file and read it. If the file
        doesn't exist, the except block returns an empty list

        :param cls: the class that we're calling the method on
        :return: A list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


