#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Prints the value as an int using the "{:d}.format()"
        print("{:d}".format(value))
        # Return true to indicate success
        return True
    except (ValueError, TypeError):
        # Returns flase if an error occurs (value is not an int)
        return False
    print()
