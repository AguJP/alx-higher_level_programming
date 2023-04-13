#!/usr/bin/python3

"""Function to return the JSON representation of an object(string)"""
import json


def to_json_string(my_obj):
    """Return JSON representatio of an object.
    Args:
        my_obj (str): The object.
    Returns:
        The JSON representation of my_obj.
    """
    return (json.dumps(my_obj))
