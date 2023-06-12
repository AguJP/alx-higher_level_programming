#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Return a list of attributes available in an object"""
    return (dir(obj))
