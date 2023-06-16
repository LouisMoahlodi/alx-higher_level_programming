#!/usr/bin/python3
""" Function that returns the a sorted list of names in the given object"""


def lookup(obj):
    """
    Returns list of available attributes and methods using 
    the built-in dir() function
    """
    return dir(obj)
