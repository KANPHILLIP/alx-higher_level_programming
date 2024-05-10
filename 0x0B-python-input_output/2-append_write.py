#!/usr/bin/python3
""" module for appends in a file """


def append_write(filename="", text=""):
    """ method that returns the number of characters added """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.append(text)
