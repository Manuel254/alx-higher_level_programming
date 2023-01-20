#!/usr/bin/python3

"""This module handles the Base class"""
import json
from os.path import exists


class Base:
    """Defines the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation

        Args:
            id (int): identity of an object

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to json string"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list of objects to file"""
        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            if list_objs is None:
                list_objs = cls.to_json_string(list_objs)
                f.write(list_objs)
            else:
                list_objs = [obj.to_dictionary() for obj in list_objs]
                list_objs = cls.to_json_string(list_objs)
                f.write(list_objs)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"

        if not exists(filename):
            return []
        else:
            with open(filename, "r") as f:
                obj_string = f.read()
                list_objs = cls.from_json_string(obj_string)
                objs = [cls.create(**dict) for dict in list_objs]
            return objs

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary != {}:
            if cls.__name__ == 'Rectangle':
                obj = cls(10, 5)
            else:
                obj = cls(5)
            obj.update(**dictionary)
            return obj
