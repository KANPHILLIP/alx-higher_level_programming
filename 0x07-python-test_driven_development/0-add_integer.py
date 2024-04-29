#!/usr/bin/python3
# 0-add_integer.py
""" module that defines integer addition
with the add_integer function.
"""


def add_integer(a, b=98):
    """returns an integer addition of a + b
    float arguments are type casted into integers before
    addition.
    Raises: TypeError if a or b are not integers
    """

    if not (isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
        return int(a) + int(b)

if __name__=="__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
