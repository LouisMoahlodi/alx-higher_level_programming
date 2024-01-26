#!/usr/bin.python3

"""

This module provides a function say_my_name that prints the full name 
composed of the given first and last names.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name composed of the given first and last names.

    Args:
        first_name (str): The first name to be printed
        last_name (str, optional): The last name to be printed

    Raises:
        TypeError: If first_name is not a string or 
        
        TypeError: If last_name is not a string

    Returns:
        None
    """
    # Check if first_name is a string
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if type(last_name) != str:
        raise TypeError("last_name must be string")
    
    else: 
        # Print the full name
        print("My name is", first_name +' '+ last_name)
