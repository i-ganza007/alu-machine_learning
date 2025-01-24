#!/usr/bin/env python3

"""
This is a function to add arrays
"""


def add_arrays(arr1, arr2):
    """
    This is to add arrays
    """
    sum = []
    if(len(arr1) != len(arr2)):
        return None
    for i in range(len(arr1)):
        sum.append(arr1[i] + arr2[i])

    return sum