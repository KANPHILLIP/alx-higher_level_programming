#!/usr/bin/python3
""" A module for a rectangle"""


class Rectangle:
    """Representaion of a rectangle"""

    def __init__(self, width=0, height=0):
        """initilize a new rectangle
        Args:

        width (int): width of the new rectangle
        height (int): height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """method that define the width of the rectangle
        Args:
        Value: width

        Raises
        TypeError: if width is not an integer
        ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """method that define the height of the rectangle
        Args:
        Value: height

        Raises
        TypeError: if height is not an integer
        ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
