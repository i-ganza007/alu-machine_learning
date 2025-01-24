#!/usr/bin/env python3
import numpy as np
def add_matrices2D(mat1, mat2):
    res1 = np.array(mat1)
    res2 = np.array(mat2)
    if res1.shape == res2.shape:
        return res1 + res2
    else:
        return None
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
