"""This script implements the binary search"""
from typing import Iterable


def bsearch(array: Iterable[int], to_be_found: int) -> int:
    """Search for an item to be found through the iterable
    by dividing it in 2 and comparing result to the item searched"""
    if array == [] or to_be_found not in array:
        raise ValueError

    first_list_index = 0
    last_list_index = sum(1 for item in array) - 1
    search_finished = False
    to_be_found_index = 0
    while first_list_index <= last_list_index and not search_finished:
        middle_list_index = (first_list_index + last_list_index) // 2
        middle_array_item = next(value for seq, value in enumerate(array)
                                 if seq == middle_list_index)
        if middle_array_item == to_be_found:
            to_be_found_index = middle_list_index
            search_finished = True
        else:
            if to_be_found < middle_array_item:
                last_list_index = middle_list_index - 1
            else:
                first_list_index = middle_list_index + 1

    return to_be_found_index
