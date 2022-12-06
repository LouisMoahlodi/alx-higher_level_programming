#!/usr/bin/python3
# def print_reversed_list_integer(my_list=[]):
    # for i in reversed(my_list):
        # print("{:d}".format(i))

def print_reversed_list_integer(my_list):
    for i in reversed(my_list):
        x = "{:d}".format(i)
        n = x.rstrip('\n')
        print(n)