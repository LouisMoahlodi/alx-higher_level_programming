#!/usr/bin/python3
import string
print(getattr(__import__('__main__'), (lambda x: x.uppercase_alphabet)(string)))
