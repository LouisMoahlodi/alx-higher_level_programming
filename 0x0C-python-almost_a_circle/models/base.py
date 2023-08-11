#!/usr/bin/python3
""" Base class created """

import json


class Base:
    """ A base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionairies):
        if list_dictionairies is None:
            return "[]"
        else:
            return json.dumps(list_dictionairies)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves a list of objects to a JSON file"""
        if list_objs is None:
            list_objs = []

        """ Get the name of the class (cls) and create the filename """
        class_name = cls.__name__
        filename = f"{class_name}.json"

        """ Convert the list of object to a list of dictionaires"""
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        """ Convert the list of dictionaries to JSON string"""
        json_string = cls.to_json_string(list_dicts)

        """ Write the JSON string to te file"""
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
