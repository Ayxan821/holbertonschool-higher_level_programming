#!/usr/bin/python3
"""
This module contains the function lookup that returns
a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object"""
    return dir(obj)
