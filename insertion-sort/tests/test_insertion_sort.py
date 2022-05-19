import unittest
from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort, MyException

def test_unsorted_list():
    lst = [2,3,5,7,13,11]
    actual = insertion_sort(lst)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_repeated_nums_unsorted_list():
    lst = [5,12,7,5,5,7]
    actual = insertion_sort(lst)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sorted_list():
    lst = [5, 5, 5, 7, 7, 12]
    actual = insertion_sort(lst)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_reversly_sorted_list():
    lst = [20,18,12,8,5,-2]
    actual = insertion_sort(lst)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

class EmptyList(unittest.TestCase):

    def test_string_input(self):
        lst = "not a list"
        self.assertRaises(MyException, insertion_sort, lst)
    
    def test_empty_list(self):
        lst = []
        self.assertRaises(MyException, insertion_sort, lst)