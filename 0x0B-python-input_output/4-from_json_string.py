#!/usr/bin/python3
""" Module defines a JSON-to-object function """


import json


def from_json_string(my_str):
    """ Returns the Python object representation of a JSON string

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't be decoded
    """

    return json.loads(my_str)
