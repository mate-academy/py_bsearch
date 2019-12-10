"""my binary search"""


def bsearch(items, value) -> int:
    """return valueError if items is not present"""
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == value:
            return mid
        if items[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError("No value!")
