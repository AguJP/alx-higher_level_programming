#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide 2 integers and print result,exception for division by 0"""
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
            print("Inside result: {}".format(quotient))
    return (quotient)
