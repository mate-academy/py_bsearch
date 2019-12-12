"""Simple binary search"""


def bsearch(arr, value):
    """
    Simple binary search
    :param arr:
    :param value:
    :return:
    """
    low = 0
    high = len(arr) - 1
    while low <= high and arr:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    raise ValueError
