def search_replace(my_list, search, replace):
    new_list = []

    #Iterate over the elements in the original list
    for element in my_list:
        # Check if the element matched the search value
        if element == search:
            # Replace the element with the new value
            new_list.append(replace)
        else:
            # Keep the original element if it doesn't match the search value
            new_list.append(element)

    return new_list