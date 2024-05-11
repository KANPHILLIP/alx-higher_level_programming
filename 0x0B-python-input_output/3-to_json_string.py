#!/usr/bin/python3
""" a module to convert to json file"""
import json


def from_json_string(my_str):
    """ method that return a object represented by
    a Json string
    """
    return json.dumps(my_str)
