#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Find the key with the max value using the max() function
    # The key parameter is set to a_dictionary.get, which gets the value
    # associated with each key
    max_key = max(a_dictionary, key=a_dictionary.get)

    return max_key
