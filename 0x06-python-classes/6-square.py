#!/usr/bin/python3
"""A module for a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size(int): The size of the new square.
            position(int, int): position of the new square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Get/set current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
