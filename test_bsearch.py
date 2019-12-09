import pytest
import bsearch


def test_empty():
    with pytest.raises(ValueError):
        bsearch.bsearch([], 0)


def test_not_found():
    with pytest.raises(ValueError):
        bsearch.bsearch([1, 2, 3], 0)


def test_even():
    assert bsearch.bsearch([1, 2, 3, 4, 5, 6, 7, 8], 2) == 1


def test_odd():
    assert bsearch.bsearch([1, 2, 3, 4, 5, 6, 7], 2) == 1


def test_dup():
    assert bsearch.bsearch([1, 2, 2, 2, 2, 2, 3, 3], 2) == 3
