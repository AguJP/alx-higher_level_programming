#!/usr/bin/python3

"""Defines a function to read a textfile"""


def read_file(filename=""):
    """Prints the contents of a UTF8 textfile to stdout
    Args:
        filename (str): The file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
