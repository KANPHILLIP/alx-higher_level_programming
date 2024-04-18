#!/usr/bin/python3
"""A module for a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initialize a new square.
        Args:
            size(int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with # value"""
        for i in range(0, self.__size):
            [print("#", end='') for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
