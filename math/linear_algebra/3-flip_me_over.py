#!/usr/bin/env python3

"""
This is a function to show transpose
"""


def matrix_transpose(arr):
    """
    Transposes a 2D matrix (nested list) by swapping rows and columns.

    Args:
        arr (list): A 2D nested list representing the matrix to transpose.

    Returns:
        list: A new 2D nested list representing the transposed matrix.

    Example:
        Input:
            [[1, 2, 3],
             [4, 5, 6]]
        Output:
            [[1, 4],
             [2, 5],
             [3, 6]]
    """
    new_arr = []  # Initialize the transposed matrix.

    # Iterate through the columns of the original matrix.
    for i in range(len(arr[0])):
        appendArr = []
        # Iterate through the rows of the original matrix.
        for j in range(len(arr)):
            appendArr.append(arr[j][i])
        new_arr.append(appendArr)

    return new_arr