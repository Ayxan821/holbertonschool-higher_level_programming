i#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    for item in reversed(my_list):
        print("{:d}".format(item))
