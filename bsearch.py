'''
Binary search algorithm
'''
from typing import Iterable


def bsearch(lst: Iterable[int], value: int) -> int:
    """l always is sorted"""
    lst = list(lst)
    start, finish = 0, len(lst) - 1
    if not lst or not value:
        raise ValueError
    while start <= finish:
        mid = (start + finish) // 2
        if value == lst[mid]:
            return mid
        if value > lst[mid]:
            start = mid + 1
        else:
            finish = mid - 1
    raise ValueError
