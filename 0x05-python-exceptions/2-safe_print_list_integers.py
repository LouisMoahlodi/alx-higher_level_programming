#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ktrack = 0

    try:
        # Iterate over the range specified by x
        for i in range(x):
            #Access the current element from my_list
            value = my_list[i]

            # Check if the element is an integer
            if isinstance(value, int):
                # Print the integer without a new line
                print("{:d}".formart(value), end="")
                # Increment counter to track number of integers printed.
                ktrack +=1
    except (IndexError, TypeError):
        # Ignore excepetions (index out of range or non-integer element)
        pass

    # Print new line after printing ints
    print()

    # Return the count of printed ints
    return ktrack