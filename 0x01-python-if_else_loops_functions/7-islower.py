#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise valueError("Input must be a single character")
    elif "a" <= c <= "z":
        return True
    else:
        return False
