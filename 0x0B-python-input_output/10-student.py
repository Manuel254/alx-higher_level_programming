#!/usr/bin/python3

"""Student to JSON"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student
        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): age of student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a student instance
        Args:
            attrs (str): List of strings
        """
        my_dict = self.__dict__
        if isinstance(attrs, list) and len(attrs) != 0:
            attrs = set(attrs)
            keys = set(my_dict.keys())
            attrs = list(attrs & keys)
            return {k: my_dict[k] for k in attrs}
        else:
            return my_dict
