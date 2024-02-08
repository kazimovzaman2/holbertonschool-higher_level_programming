#!/usr/bin/python3


"""Documented Module"""


def pascal_triangle(n):
    """Function Document"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                above = triangle[i - 1]
                elem = above[j - 1] + above[j]
                row.append(elem)
        triangle.append(row)

    return triangle
