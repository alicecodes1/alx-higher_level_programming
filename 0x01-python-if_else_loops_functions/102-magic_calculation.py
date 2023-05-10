#!/usr/bin/python3
def magic_calculatin(a, b, c):
    if a < b:
        return c
    if b < c:
        return a + b
    return a * b - c
