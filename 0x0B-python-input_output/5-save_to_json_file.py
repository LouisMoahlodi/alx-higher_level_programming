#!/usr/bin/python3
""" Module defines a JSON file-writing function """

import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file using JSON format

    Args:
        my_obj: object
        filename: text file name

    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
