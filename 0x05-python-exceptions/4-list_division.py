#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Empty list to store the division results
    results = []
    # Iterate over the range specified by list_length
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]

        except TypeError:
            print("wrong type")
            div_result = 0

        except ZeroDivisionError:
            # Print message if division by zero occurs
            print("division by 0")
            div_result = 0

        except IndexError:
            print("out of range")
            div_result = 0

        finally:
            # Append each result into a new list
            results.append(div_result)
    # Return the resulting list of divisions
    return results
