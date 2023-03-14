#!/bin/usr/python3

def element_at(my_list, idx):
    """Function to retrieve an element from a list like in C"""
    if (idx < 0) || (idx >= len(my_list)):
        return (None)
    return (my_list[idx])