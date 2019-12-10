"""
test docstring
"""

import pytest
import bsearch


def test_empty():
    """
    test if list is empty
    :return:
    """
    with pytest.raises(ValueError):
        bsearch.bin_search([], 0)


def test_not_found():
    """
    test if number equals 0
    :return:
    """
    with pytest.raises(ValueError):
        bsearch.bin_search([1, 2, 3], 0)


def test_even():
    """
    find 2 in the list
    :return:
    """
    assert bsearch.bin_search([1, 2, 3, 4, 5, 6, 7, 8], 2) == 1


def test_odd():
    """
    find 2 in the list
    :return:
    """
    assert bsearch.bin_search([1, 2, 3, 4, 5, 6, 7], 2) == 1


def test_dup():
    """
    find 2 in the list
    :return:
    """
    assert bsearch.bin_search([1, 2, 2, 2, 2, 2, 3, 3], 2) == 3
