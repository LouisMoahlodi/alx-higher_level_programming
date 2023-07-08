#!/usr/bin/python3
""" A Function that checks is instance of a class or an inherited class """



def is_kind_of_class(obj, a_class):
    """ Returns the true is instance of the class or the inherited class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
    