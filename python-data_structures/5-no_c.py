#!/usr/bin/python3


def no_c(my_string):
    """Return a copy of my_string without any 'c' or 'C' characters."""
    new_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
