#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for idx, i in reversed(range(len(my_list))):
        print("{:d}".format(idx, i))
