#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Executes a function safely, returns the result of the function
    if successful, else an exception occurs"""
    try:
        func = fct(*args)
        return (func)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
