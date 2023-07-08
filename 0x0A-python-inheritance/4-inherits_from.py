#!/usr/bin/python3
""" A Function that check if the object inherits from the class"""


def inherits_from(obj, a_class):
    """
        Returns True if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class;
       otherwise False.
    """
    return isinstance(a_class(), obj.__class__) or issubclass(type(obj))