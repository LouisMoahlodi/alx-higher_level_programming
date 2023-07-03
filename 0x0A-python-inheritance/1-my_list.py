#!/usr/bin/pyhton3
""" A class that inherits from another class"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
