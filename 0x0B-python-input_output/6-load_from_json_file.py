#!/usr/bin/python3
""" load from json module """
import json


def load_from_json_file(filename):
    """ method that loads a json file to an object """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f)
