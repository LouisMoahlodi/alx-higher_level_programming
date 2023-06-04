#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Initialie an empty dictionary to store the multiplied values
    new_dict = {}

    # Iterate over the key-value pairs in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and assign it to the corresponding key in the
        # new dictionary
        new_dict[key] = value * 2

    return new_dict
