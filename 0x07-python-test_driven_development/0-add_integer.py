#!/usr/bin/python3
# 0-add_integer.py
""" module for add_integer method"""


def add_integer(a, b=98):

    """returns an integer addition of a + b
    float arguments are type casted into integers before
    addition.

    Args:
    a: the first integer
    b: the second integer with a default value of 98

    Raises: TypeError if a or b are not integers
    """

    if not (isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
        return (int(a) + int(b))


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/0-add_integer.txt")
