#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints first x elements of a list, only integers
    Exception occurs if x is bigger than length of my_list"""
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
