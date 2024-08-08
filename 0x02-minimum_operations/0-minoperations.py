#!/usr/bin/python3

def minOperations(n):
    opps, text = 0, 'H'
    while len(text) != n and n > 1:
        if n % len(text) == 0:
            copy = text[:]
            text += copy
            opps += 2
        else:
            text += copy
            opps += 1
    return opps
