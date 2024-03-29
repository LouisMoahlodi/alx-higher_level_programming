#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Variable to keep track of the number of succesfully printed elements
    ktrack = 0

    for i in range(x):  # Loop through the specified range
        try:
            # Prints the current element wihtout a new line
            print(f"{my_list[i]}", end="")
            ktrack += 1  # Increments counter if successfuly printed
        except IndexError:
            # print("Nope: try again chief")
            break  # Exit the loop if index is out of range
    print()  # Print a new line after printin the element
    return ktrack
