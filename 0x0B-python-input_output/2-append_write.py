#!/usr/bin/python3

"""Function to append a string to a textfile"""


def append_write(filename="", text=""):
    """Append a string to a text file.
    Args:
        filename (str): The name of the file to append.
        text (str): The string to append to the file.
    Returns:
        The no. of characters appended.
    """
    with open(filename, "a", encoding="utf-8")as f:
        return f.write(text)
