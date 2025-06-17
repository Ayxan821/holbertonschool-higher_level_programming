#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replaces element at given index in a list, if index is valid."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
