#!/usr/bin/python3
"""module for same_class method """


def is_same_class(obj, a_class):

    '''method that checks if an object
    is exacty the same instance of the 
    class specified
    '''
    return type(obj) == a_class
