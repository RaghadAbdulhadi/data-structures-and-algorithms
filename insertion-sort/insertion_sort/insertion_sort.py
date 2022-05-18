class MyException(Exception):
    pass

def insertion_sort(lst):
    """
    A function that takes in a list of numbers and sorts them inplace using the insertion sort algorithm
        Arguments: list
        Returns: sorted list
    """
    if type(lst) == str:
        raise MyException("The input should be a list of numbers")
    if len(lst) == 0:
        raise MyException("List is empty, the input should be a list of numbers")
    for current_index in range(1, len(lst)):
        next_value = lst[current_index] 
        # print('before', next_value)
        # print(current_index)

        while current_index > 0 and next_value < lst[current_index - 1]:
            # print('after', next_value)
            lst[current_index] = lst[current_index - 1]
            current_index = current_index - 1
            # print("inside", current_index)
        lst[current_index] = next_value
        # print(current_index)

    return lst







if __name__ == "__main__":
    lst = [5,12,7,5,5,7]
    lst_1 = [20,18,12,8,5,-2]
    lst_2 = [2,3,5,7,13,11]
    # lst_3 = []
    # lst_4 = "not a list"
    lst_5 = [8,4,23,42,16,15]

    # print(insertion_sort(lst))
    # print(insertion_sort(lst_1))
    # print(insertion_sort(lst_2))
    # print(insertion_sort(lst_3))
    # print(insertion_sort(lst_4))
    print(insertion_sort(lst_5))
