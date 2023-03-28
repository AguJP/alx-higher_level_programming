#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide 2 integers and print result,exception for division by 0"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
            print("Inside result: {}".format(div))
    return (div)
