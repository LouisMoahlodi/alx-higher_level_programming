#!/usr/bin/python3
def safe_print_intger(value):
        try: 
            # Prints the value as an int using the "{:d}.format()"
            print("{:d}".format(value))
            print()
            # Return true to indicate success
            return True 
        except (ValueError, TypeError):
              # Returns flase if an error occurs (value is not an int)
              return False