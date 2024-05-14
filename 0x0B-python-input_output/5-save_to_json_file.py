#!/usr/bin/python3
""" save to json module """
import json


def save_to_json_file(my_obj, filename):
    """ method that saves to json file"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
