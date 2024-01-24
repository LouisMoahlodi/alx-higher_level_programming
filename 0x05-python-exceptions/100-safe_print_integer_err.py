#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        # Try to convert the value to an integer
        int_value = int(value)

        # IF successful, print the int followed by a new line
        print("{:d}".format(int_value))

        # Return True indicating successful printing
        return True

    except Exception as e:
        # IF there is an exception, prin the error msg to stderr
        sys.stderr.write("Exception: {}\n".format(e))

        # Return False to show failure
        return False
