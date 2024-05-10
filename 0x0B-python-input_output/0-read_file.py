#!/usr/bin/python3
""" module that reads a text file """


def read_file(filename=""):
    """ raed_file method """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end='')
