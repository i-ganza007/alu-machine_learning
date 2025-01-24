#!/usr/bin/env python3

"""
This module provides functions for calculating matrix shapes.
"""


def matrix_shape(arr):
    """
    Calculates the shape of a matrix (nested list) as a list of integers.

    Args:
        arr (list): A nested list representing the matrix.

    Returns:
        list: The shape of the matrix as a list of integers.
    """
    shape = []

    def check_arr_size(current_arr):
        if isinstance(current_arr, list):
            shape.append(len(current_arr))
            check_arr_size(current_arr[0])

    check_arr_size(arr)
    return shape
