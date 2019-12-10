"""
Module binary search
"""
from typing import Iterable


def bsearch(lst: Iterable[int], value: int):
    """
    Binary search implementation
    :param lst: Iterable[int]
    :param value: int
    :return: int
    """

    if not lst or value == 0:
        raise ValueError

    array = sorted(lst)

    lower, high = 0, len(array) - 1
    while lower <= high:
        mid = (lower + high) // 2
        if array[mid] < value:
            lower = mid + 1
        elif value < array[mid]:
            high = mid - 1
        else:
            return mid
    return None
