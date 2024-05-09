#!/usr/bin/python3
""" a module of is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """ Determine if the object is an instance of,
    or if the object is an instance of a
    that inherited from, the specified class
    """
    return isinstance(obj, a_class)
