"""binary search algorithm"""
from typing import Iterable


def bsearch(list_: Iterable[int], value: int) -> int:
    """
    :param list_: sorted list of integers
    :param value: value to search
    :return: position of searched value in list
    :raise ValueError if list is empty or value not in list
    """
    if not list:
        raise ValueError
    arr = list(list_)
    start, end = 0, len(list(arr)) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == value:
            return middle
        if arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
    raise ValueError
