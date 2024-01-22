#!/usr/bin/python3
import sys
import stderr


def safe_print_integer_err(value):
    try:
        # Try to convert the value to an integer
        int_value = int(value)

        # IF successful, print the int followed by a new line
        print("{:d}".format(int_value))

        # Return True indicating successful printing
        return True

    except Exception as e:
        # IF there is an exception, prin the error msg to stderr
        print("Exception: {}".format(e), file=stderr)

        # Return False to show failure
        return False
