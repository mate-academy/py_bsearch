"""
Implement binary search algorithm
(https://en.wikipedia.org/wiki/Binary_search_algorithm).
"""


from typing import Iterable


def bsearch(arr: Iterable[int], value: int) -> int:
    """binary search algorithm"""
    if not arr:
        raise ValueError
    arr = list(arr)
    left = 0
    right = len(list(arr)) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            right = mid
        else:
            left = mid
    raise ValueError
