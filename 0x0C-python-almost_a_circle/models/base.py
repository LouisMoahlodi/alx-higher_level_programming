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
        """Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries extracted from the JSON string.
        """
        if json_string is None:
            json_string = []
            return json_string
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set from a dictionary.

        Args:
            **dictionary: Keyword arguments representing instance attributes.

        Returns:
            Base: An instance with attributes set from the dictionary.
        """
        dummy_instance = None
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        if dummy_instance is not None:
            if 'id' in dictionary:
                dummy_instance.update(**dictionary)
            return dummy_instance
        return None

    @classmethod
    def load_from_file(cls):
        """ Loads and returns a list of instance from a JSON file.

        Returns:
            list: List of instances loaded from the JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                intances = [cls.create(**data) for data in list_dicts]
                return intances
        # If there's no such file then just return empty list
        except FileNotFoundError:
            return []
