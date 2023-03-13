#!/usr/bin/python3

"""Print the alphabet in reverse, alternating lower and upper case"""
i = 0
for c in range(ord('z'), ord('a') - 1, - 1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
