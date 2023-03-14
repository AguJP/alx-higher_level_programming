#!/usr/bin/python3

def multiple_returns(sentence):
    """Return a tuple with the lenght of a string and its first char"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
