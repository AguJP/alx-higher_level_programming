#!/usr/bin/python3

"""Function to create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename) as f:
        return (json.load(f))
