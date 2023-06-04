def roman_to_int(roman_string):
    # Check if the input is not a string or if it is None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    # Define a dictionary to map Roman nemerls to their corresponding integers values
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Create a list of integer values by mapping the lambda function to each character of the Roman numeral string
    values = list(map(lambda char: roman_numerals.get(char, 0), roman_string))

    # Initialize variables to store the result and previous value
    result = 0
    previous_value = 0

    # Iterate through each value in the list of integer values in reverse order
    for value in values[::-1]:
        # Compare the current value with the previous value
        if value >= previous_value:
            # If the current value is greater than or equal to the previous value, add it to the result
            result += value
        else:
            # IF the current value is smaller than the previous value, subtact it from the result
            result -= value

        # Update the previous value for the next iteration
        previous_value = value

    return result
