#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exist  in the dictionary
    if key in a_dictionary:
        # If the key exist, delete the key-value pair using the 'de;' statement
        del a_dictionary[key]
    return a_dictionary
