#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {}
    sorted_keys = sorted(a_dictionary.key())

    for key in sorted_keys:
        sorted_dict[key] = a_dictionary[key]

    return sorted_dict 