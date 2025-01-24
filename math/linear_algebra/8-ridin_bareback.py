#!/usr/bin/env python3
import numpy as np
def mat_mul(mat1, mat2):
    res1 = np.array(mat1)
    res2 = np.array(mat2)
    if list(res1.shape)[-1] == list(res2.shape)[0] :
        return res1 @ res2
    
    else:
        return None
mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mat_mul(mat1, mat2))
