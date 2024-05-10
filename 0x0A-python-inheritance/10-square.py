#!/usr/bin/python3
"""module for a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a subclass of Rectangle """
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area method"""
        return (self.__size * self.__size)
