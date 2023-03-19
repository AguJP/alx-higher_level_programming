#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list, only once"""
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
