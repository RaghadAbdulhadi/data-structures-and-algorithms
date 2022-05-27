from quick_sort.quick_sort import quick_sort, MyException


def test_quick_reverse_sort():
    actual = quick_sort([20,18,12,8,5,-2], 0, 5)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected