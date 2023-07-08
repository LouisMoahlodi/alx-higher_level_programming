#!/usr/bin/python3
""" A Function that check if the object inherits from the class"""


def inherits_from(obj, a_class):
    """ Returns true if the object inherits from a_class"""
    return isinstance(a_class(), obj.__class__) or issubclass(type(obj))