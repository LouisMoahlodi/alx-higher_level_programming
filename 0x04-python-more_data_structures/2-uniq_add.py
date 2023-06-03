#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    uniq_ints = set()

    # Iterate over the element in the list
    for element in my_list:
        # Check if the element is an integer
        if isinstance(element, int):
            # Add the int to the set
            uniq_ints.add(element)

    # Calculate the sum of uniwque integers
    sum_unique = sum(uniq_ints)

    return sum_unique