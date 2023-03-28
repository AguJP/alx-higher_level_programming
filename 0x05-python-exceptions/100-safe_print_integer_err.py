#!/usr/bin/python3

def safe_print_integer_err(value):
    """Prints an integer. Exception occurs if `value` is not integer"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)