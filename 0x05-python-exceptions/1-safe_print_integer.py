#!/usr/bin/phython3

def safe_print_integer(value):
    """Prints an integer with "{:d}".format().
    Return `False` if TypeError/ValueError occurs, else True"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
