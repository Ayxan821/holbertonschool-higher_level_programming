#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Return copy of list with element replaced at idx if idx is valid.

    If idx is negative or out of range, return copy of original list.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
