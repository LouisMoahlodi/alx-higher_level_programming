#!/usr/bin/pyhton3 
def list_division(my_list_1, my_list_2, list_length):
    #Empty list to store the division results
    results = []

    try:
        # Iterate over the range specified by list_length
        for i in range(list_length):
            try:
                # Access the current element from my_list_1
                value_1 = my_list_1[i]
                # Access the current element from my_list_2
                value_2 = my_list_2[i]

                # Check if both values are int or float
                if isinstance(value_1, (int, float)) and isinstance(value_2, (int, float)):
                    try:
                        div_result = value_1 / value_2
                        # Append the division result to the list
                        results.append(div_result)
                    except ZeroDivisionError:
                        # Print message if division by zero occurs
                        print("division by zero")
                        # Append 0 to the result list
                        results.append(0)
                    else:
                        print("wrong type")
                        results.append(0)
            except IndexError:
                print("out of range")
                results.append(0)
    except TypeError:
        # Ignore TyperError exceptions
        pass

    # Return the resulting list of divisions
    return results