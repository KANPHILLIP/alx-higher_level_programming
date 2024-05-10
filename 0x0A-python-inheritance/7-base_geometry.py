#!/usr/bin/python3
""" a module for the BaseGeometry class """


class BaseGeometry:
    """ Represents BaseGeometry class """

    def area(self):
        """ method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
