#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Return a new list with the element at idx replaced by element if idx valid.

    If idx is invalid (negative or out of range), returns a copy of the original list.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
