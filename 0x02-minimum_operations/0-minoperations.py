#!/usr/bin/python3
""" Module for minoperations"""


def minOperations(n):
    """
    minOperations
    """
    if (n < 2):
        return 0
    ops, base = 0, 2
    while base <= n:
        if n % base == 0:
            ops += base
            n = n / base
            base -= 1
        base += 1
    return ops