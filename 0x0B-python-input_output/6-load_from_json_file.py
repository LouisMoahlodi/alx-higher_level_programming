#!/usr/bin/python3
""" Module that creates an Object from JSON file """

import json


def load_from_json_file(filename):
    """ Function creates a Python object from given JSON files

    Args:
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
