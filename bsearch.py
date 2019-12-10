"""Binary search algorithm module"""

from typing import Iterable


def bsearch(array: Iterable[int], value: int):
    """Binary search algorithm function
    array - the array where the search is performed
    value - what we are looking for
    return: value index
    """
    if not array or not value:
        raise ValueError
    array = list(array)
    low = 0
    height = len(array) - 1
    result = None
    while low <= height:
        center = low + (height - low) // 2
        print(height, low, center)
        if value < array[center]:
            height = center - 1
        elif value > array[center]:
            low = center + 1
        else:
            result = center
            break
    return result
