"""
Module with implementation of binary search
Functions
---------
bsearch()
"""
from typing import Iterable


def bsearch(array: Iterable[int], lost: int) -> int:
    """
    Return position of 'lost' in the array
    :array: Iterable[int]
    :lost: int
    """

    arr = list(array)
    if not arr or lost not in arr:
        raise ValueError
    left = 0
    right = len(arr)
    middle = 0
    while right - left > 1:
        middle = (right + left) // 2
        if lost < arr[middle]:
            right = middle
        elif lost > arr[middle]:
            left = middle
        else:
            return middle
    return middle
