"""binary search recursive algorithm"""
from typing import List


def bsearch(list_: List[int], value: int) -> int:
    """
    :param list_: sorted list of integers
    :param value: value to search
    :return: call of binary search function
    :raise ValueError if list is empty
    """
    start = 0
    end = len(list_) - 1
    if not list_:
        raise ValueError

    def search(arr: List[int], key: int, start_: int, end_: int) -> int:
        """
        :param arr: list of integers
        :param key: value to search
        :param start_: first index of sublist
        :param end_: last index if sublist
        :return: index of searched value
        :raise: ValueError if searched value not in list
        """
        mid = (start_ + end_) // 2
        if arr[mid] == key:
            return mid
        if start_ >= end_:
            raise ValueError
        if arr[mid] > key:
            return search(arr, key, start_, arr[mid] - 1)
        if arr[mid] < key:
            return search(arr, key, arr[mid] + 1, end_)
        raise ValueError

    return search(list_, value, start, end)
