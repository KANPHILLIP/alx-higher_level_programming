#!/usr/bin/python3
""" module for writing in a file """


def write_file(filename="", text=""):
    """ method that returns the number of characters written """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write()
