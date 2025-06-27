#!/usr/bin/python3
"""This module defines a class MyList that inherits from list and adds a method to print the list sorted."""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
