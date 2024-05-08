#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ Represents a class that inherites from the list module"""
    def print_sorted(self):
        """method for printing sorted list"""
        print(sorted(self))
