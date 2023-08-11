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
