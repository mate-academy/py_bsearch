"""
implement binary search
"""


def bin_search(lst, num: int) -> int:
    """

    :param lst:
    :param num:
    :return:
    """
    if len(lst) == 0 or num == 0:
        raise ValueError
    first = 0
    last = len(lst) - 1
    mid = 0
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] != num:
            if num < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
        elif lst[mid] == num:
            break
    return mid
