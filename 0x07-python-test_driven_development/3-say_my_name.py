#!/usr/bin/python3
""" module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """function that print first and last name
    Args:
    first_name: first name has to be a string
    last_name: last name has to be a string

    Raises:
    TypeError: if first_name and last_name are not strings

    Return: first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

        return "My name is {:s} {:s}".format(first_name, last_name)


if __name__ == "__main__":

    import doctest
    doctest.test.file("test/3-say_my_name.txt")
