#!/usr/bin/python3 
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the unique element
    unique_set = set()

    # Iterate over the element in set_1
    for element in set_1:
        if element not in set_2:
            unique_set.add(element)

    for element in set_2:
        if element not in set_1:
            unique_set.add(element)

    return unique_set