#!/usr/bin/python3
""" from json to string module """
import json


def from_json_string(my_str):
    """ method that converts a string to json """
    return json.loads(my_str)
