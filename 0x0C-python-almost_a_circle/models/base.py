#!/usr/bin/python3

"""This module handles the Base class"""
import json
import csv
from os.path import exists
from turtle import *


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
    def save_to_file_csv(cls, list_objs):
        """Saves data to csv"""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']

                csv_writer = csv.DictWriter(f, fieldnames=fields)

                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads data from csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == 'Rectangle':
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                csv_r = csv.DictReader(f, fieldnames=fields)
                csv_r = [dict([k, int(v)] for k, v in d.items())
                         for d in csv_r]
                return [cls.create(**d) for d in csv_r]
        except IOError:
            return []

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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares on screen"""
        getscreen()
        title("Rectangles and Squares")
        bgcolor("#c0c0c0")

        for r in list_rectangles:
            penup()
            goto(r.x, r.y)
            pendown()
            for i in range(2):
                fd(r.width)
                rt(90)
                fd(r.height)
                rt(90)

        for s in list_squares:
            penup()
            goto(s.x, s.y)
            pendown()
            for i in range(4):
                fd(s.size)
                rt(90)
