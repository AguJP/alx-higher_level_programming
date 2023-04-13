#!/usr/bin/python3

"""Function to return an object(Python data structure) represented by a
    JSON string"""
import json


def from_json_string(my_str):
    """Returns an object(Python data structure)rep. by a JSON string"""
    return (json.loads(my_str))
