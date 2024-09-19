#!/usr/bin/env python3
"""
Module `4-inverse`
This module calculates the inverse of a given square matrix
"""


def inverse(matrix):
    """
    Calculate the inverse of a given square matrix.

    The inverse A^(-1) of a matrix A is such that A * A^(-1) = A^(-1) * A = I,
    where I is the identity matrix.

    Args:
    matrix (list of lists): The input matrix whose inverse is
    to be calculated.
    Each inner list represents a row of the matrix.

    Returns:
    list of lists or None: The inverse of the input matrix,
    or None if the matrix is singular.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the input matrix is not square or is empty.
    """

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    def minor(mat, i, j):
        """Calculate the minor of matrix mat for element at (i, j)."""
        return [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

    def determinant(mat):
        """Calculate the determinant of a matrix."""
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(len(mat)):
            det += ((-1) ** j) * mat[0][j] * determinant(minor(mat, 0, j))
        return det

    det = determinant(matrix)

    if det == 0:
        return None

    if n == 1:
        return [[1 / matrix[0][0]]]

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor_det = determinant(minor(matrix, i, j))
            cofactor_row.append((-1) ** (i + j) * minor_det)
        cofactor_matrix.append(cofactor_row)

    adjugate_matrix = [[cofactor_matrix[j][i]
                        for j in range(n)] for i in range(n)]

    inverse_matrix = [[adjugate_matrix[i][j] /
                       det for j in range(n)] for i in range(n)]

    return inverse_matrix
