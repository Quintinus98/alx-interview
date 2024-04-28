#!/usr/bin/python3
"""
Pascal's triangle implementation with python
"""


def factorial(k):
    """
    Factorial formula
    """
    if k <= 1:
        return 1
    return factorial(k - 1) * k


def pascal_formula(n, m):
    """
    Pascal's triangle formaula
    """
    if n == 0:
        return 1
    return factorial(n) // (factorial(n - m) * factorial(m))


def pascal_triangle(n):
    """
    Create pascal's triangle
    """
    pascals = []
    if n == 0:
        return pascals
    for k in range(0, n):
        iter = [pascal_formula(k, i) for i in range(0, k + 1)]
        pascals.append(iter)
    return pascals


if __name__ == "__main__":
    pascal_triangle()
