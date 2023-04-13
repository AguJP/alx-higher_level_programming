#!/usr/bin/python3

"""Function to write a string to a text file, returns no. of chars written"""


def write_file(filename="", text=""):
    """write to a text file utf-8.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The no. of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
