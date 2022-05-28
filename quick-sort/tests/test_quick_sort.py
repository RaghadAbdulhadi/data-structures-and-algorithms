import unittest
from quick_sort.quick_sort import quick_sort, MyException


def test_quick_reverse_sort():
    actual = quick_sort([20,18,12,8,5,-2], 0, 5)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_quick_nearly_sort():
    actual = quick_sort([5,12,7,5,5,7], 0, 5)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_quick_unique_sort():
    actual = quick_sort([2,3,5,7,13,11], 0, 5)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_quick_all_values_are_equal_sort():
    actual = quick_sort([0, 0, 0, 0, 0, 0], 0, 5)
    expected = [0, 0, 0, 0, 0, 0]
    assert actual == expected

class Emptylist(unittest.TestCase):
    def test_quick_sort_empty_lst(self):
        lst = []
        start = 0
        end = 4
        self.assertRaises(MyException, quick_sort, lst, start,end)
