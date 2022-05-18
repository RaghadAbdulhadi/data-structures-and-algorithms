def reverse_array(arr):
    """
    Function that reverse the elements of a list
    Input: List 
    Output: Returns list of reversed elements

    """

    arr_reversed = [None] * len(arr)
    start_index = 0
    index = len(arr)-1
    while index > -1:
        arr_reversed[start_index] = arr[index]
        index -= 1
        start_index += 1
    return arr_reversed

reverse_array(arr)

