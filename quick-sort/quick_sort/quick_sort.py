class MyException(Exception):
    pass

def partition(lst, start, end):
    """
    A function that is used to rearrange the array, and return the index of pivot
        Arguments: list, start index, end index
        Returns: Pivot Index
    """
    pivot = lst[end]
    pivot_index = start
    for i in range(start, end):
        if lst[i] <= pivot:
            lst[i], lst[pivot_index] = lst[pivot_index], lst[i]
            pivot_index += 1
    lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
    return pivot_index

def quick_sort(lst, start, end):
    """
    A function that is used to sort the elements of the list in place
        Arguments: List, start index, end index
        Returns: Sorted list
    """
    if len(lst) == 0:
        raise MyException("List is empty")

    if start < end:
        pivot_index = partition(lst, start, end)
        quick_sort(lst, start, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, end)
    return lst


if __name__ == '__main__':
    # print(quick_sort([20,18,12,8,5,-2], 0, 5))
    print(quick_sort([5,12,7,5,5,7], 0, 5))
    # print(quick_sort([8,4,23,42,16,15], 0, 5))
    # print(quick_sort([0,0,0,0,0,0], 0, 5))
    # print(quick_sort([], 0, 5))

