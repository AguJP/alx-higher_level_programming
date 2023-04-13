#!/usr/bin/python3

"""Function to write an object to a textfile using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON.
    Args:
        my_obj (obj): The object
        filename (str): The name of text file.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
