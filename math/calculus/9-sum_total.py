#!/usr/bin/env python3
"""
This script contains a function to calculate the sum of the squares of the first n natural numbers.
"""


def summation_i_squared(n):
    """
    This function calculates the sum of the squares of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to sum.

    Returns:
    int: The sum of the squares of the first n natural numbers. Returns None if n is not an integer.
    """
    if n != int:
        return None
    total = sum(i**2 for i in range(1, n + 1))
    return total
