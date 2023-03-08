#!/usr/bin/pyhton3
"""

This module is composed by a function that adds two numbers

"""

def add_integer(a, b=98):
    """ a function that adds 2 integers 
    
    Args:
        a: first argument
        b: second argument

    Returns:
            Sum of the two arguments

    Raises:
            TypeError: If either of the arguments not an integer or a float

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
