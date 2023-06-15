#!/usr/bin/python3
def safe_print_list (my_list=[], x=0):
    try:
        # Print the elements on the same line
        for i in range(x):
            print(my_list[i])
        print() #prints a new line
    except IndexError:
        print("Nope: try again chief")