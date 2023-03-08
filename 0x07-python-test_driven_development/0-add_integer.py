#!/usr/bin/pyhton3
"""

his module is composed of a function called 'add_integer' that takes two arguments, 'a' and 'b', and returns their sum.
"""

def add_integer(a, b=98):
    """
    Args:
      a (int or float): First argument to be added.
      b (int or float, optional): Second argument to be added. Defaults to 98.

    Returns:
     int: The sum of 'a' and 'b' as an integer.

    Raises:
        TypeError: If either of the arguments is not an integer or a float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
