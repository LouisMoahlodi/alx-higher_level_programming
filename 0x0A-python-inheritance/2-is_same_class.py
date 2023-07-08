#!/usr/bin/python3
""" A Function that returns  True if the object is of specified class"""


def is_same_class(obj, a_class):
    """ Get the class of the object using the type functions"""
    obj_class = type(obj)

    # Compare the the object's class with the specified class
    if obj_class is a_class:
        return True
    else:
        return False
    