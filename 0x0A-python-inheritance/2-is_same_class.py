#!/usr/bin/python3
def is_same_class(obj, a_class):

    '''method that checks if an object
    is exacty the same instance of the 
    class specified
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
