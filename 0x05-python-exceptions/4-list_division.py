#!/usr/bin/python3 
def list_division(my_list_1, my_list_2, list_length):
    # Empty list to store the division results
    results = []
    # Iterate over the range specified by list_length
    for i in range(list_length):
        try:
            # Access the current element from my_list_1
            value_1 = my_list_1[i]
            # Access the current element from my_list_2
            value_2 = my_list_2[i]
            div_result = value_1 / value_2
        except ZeroDivisionError:
            # Print message if division by zero occurs
            print("division by zero")

        except TypeError:
            print("wrong type")
            div_result = 0
        
        except IndexError:
            print("out of range")
            div_result = 0
            
        finally:
            # Append each result into a new list
            results.append(div_result)
    # Return the resulting list of divisions
    return results
