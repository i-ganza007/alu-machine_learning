#!/usr/bin/env python3
import numpy as np
def add_arrays(arr1, arr2):
    res1 = np.array(arr1)
    res2 = np.array(arr2)
    if res1.shape == res2.shape:
        return res1 + res2
    else:
        return None
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))
